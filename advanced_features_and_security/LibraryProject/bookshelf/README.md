# Permissions and Groups Setup

## Custom Permissions

The `CustomUser` model has the following custom permissions:

- `can_view`: Can view user
- `can_create`: Can create user
- `can_edit`: Can edit user
- `can_delete`: Can delete user

## Groups

The following groups are set up with the corresponding permissions:

- `Editors`: `can_view`, `can_create`, `can_edit`
- `Viewers`: `can_view`
- `Admins`: `can_view`, `can_create`, `can_edit`, `can_delete`

## Enforcing Permissions in Views

Permissions are enforced in views using the `@permission_required` decorator. For example:

```python
@permission_required('bookshelf.can_edit', raise_exception=True)
def user_edit(request, user_id):
    # View logic
```
