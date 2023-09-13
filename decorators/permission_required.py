# Декоратор для проверки прав доступа может быть особенно полезным в веб-приложениях,
# где некоторые действия могут быть ограничены для определенных групп пользователей.
# Базовый пример декоратора, который проверяет,
# имеет ли пользователь право на выполнение функции:

def permission_required(permission):
    def decorator(func):
        def wrapper(user, *args, **kwargs):
            if user.get('permission') != permission:
                raise PermissionError(f"Пользователь {user.get('name')} не имеет разрешения {permission} для выполнения этой операции.")
            return func(user, *args, **kwargs)

        return wrapper

    return decorator


@permission_required('admin')
def restricted_function(user):
    print(f"Доступ разрешен для {user.get('name')}.")


user1 = {'name': 'Алексей', 'permission': 'admin'}
user2 = {'name': 'Мария', 'permission': 'user'}

restricted_function(user1)  # Должно работать без ошибок
restricted_function(user2)  # Должно вызвать ошибку PermissionError
