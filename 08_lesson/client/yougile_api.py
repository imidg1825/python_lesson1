import os
from typing import Any, Dict, Optional

import requests


class YougileAPI:
    def __init__(self) -> None:
        base_url = os.environ.get("YOUGILE_BASE_URL")
        token = os.environ.get("YOUGILE_API_TOKEN")

        if not base_url:
            raise RuntimeError("YOUGILE_BASE_URL is not set")
        if not token:
            raise RuntimeError("YOUGILE_API_TOKEN is not set")

        self.base_url = base_url.rstrip("/")
        self.token = token.strip()

    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def _request(
        self,
        method: str,
        path: str,
        json: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        url = f"{self.base_url}{path}"
        return requests.request(
            method=method,
            url=url,
            headers=self._headers(),
            json=json,
            timeout=20,
        )

    # ---------- helpers ----------
    @staticmethod
    def _extract_first_user_id(data: Any) -> str:
        # case 1: list of users
        if (
            isinstance(data, list)
            and data
            and isinstance(data[0], dict)
            and "id" in data[0]
        ):
            return str(data[0]["id"])

        # case 2: dict with list inside (common paginated formats)
        if isinstance(data, dict):
            for key in ("content", "items", "data", "users", "results"):
                value = data.get(key)
                if (
                    isinstance(value, list)
                    and value
                    and isinstance(value[0], dict)
                    and "id" in value[0]
                ):
                    return str(value[0]["id"])

            # case 3: dict of objects {something: {...}} - take first dict value with id
            for value in data.values():
                if isinstance(value, dict) and "id" in value:
                    return str(value["id"])

        raise RuntimeError(f"Cannot extract user id from response: {data}")

    def get_any_user_id(self) -> str:
        r = self._request("GET", "/api-v2/users")
        r.raise_for_status()
        return self._extract_first_user_id(r.json())

    # ---------- projects ----------
    def create_project(self, title: str) -> requests.Response:
        user_id = self.get_any_user_id()
        payload = {"title": title, "users": {user_id: "admin"}}
        return self._request("POST", "/api-v2/projects", json=payload)

    def update_project(self, project_id: str, title: str) -> requests.Response:
        return self._request(
            "PUT",
            f"/api-v2/projects/{project_id}",
            json={"title": title},
        )

    def get_project(self, project_id: str) -> requests.Response:
        return self._request("GET", f"/api-v2/projects/{project_id}")
