from app.handlers.users import main, menu

user_routers = [
    main.router,
    menu.router
]
