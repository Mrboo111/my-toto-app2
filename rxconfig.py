import reflex as rx

config = rx.Config(
    app_name="my_todo_app2",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)