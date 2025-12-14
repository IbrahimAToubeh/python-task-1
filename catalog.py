from typing import List, Any
from .resources import Resource

class ResourceCatalog:
    def __init__(self):
        self._resources = []

    def add_resource(self, resource: Resource):
        self._resources.append(resource)

    def allocate(self, target: Any, resource_type: str) -> bool:
        if hasattr(target, 'needs_resource') and hasattr(target, 'name'):
            for res in self._resources:
                if res.status == "available" and res.type == resource_type:
                    res.status = "allocated"
                    print(f"Allocated {res.id} ({res.type}) to {target.name}")
                    return True
            print(f"No {resource_type} available for {target.name}")
            return False
        else:
            print("Target does not support resource allocation.")
            return False

    def __len__(self):
        return len(self._resources)

    def __iter__(self):
        return iter(self._resources)
