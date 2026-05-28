import reflex as rx

# 状態（State）の定義：Reactの useState のようなもの
class State(rx.State):
    items: list[str] = ["Pythonを学ぶ", "ReflexでWebサイトを作る"]
    new_item: str = ""

    def add_item(self):
        if self.new_item:
            self.items.append(self.new_item)
            self.new_item = ""  # 入力欄をクリア

    def delete_item(self, item: str):
        self.items.remove(item)


# 画面（UI）の定義：Reactコンポーネント風の記述
def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("My Todo App (Python + React)", size="8", color_scheme="indigo"),
            rx.text("Pythonだけで作ったReact風のToDoアプリです。"),
            
            rx.divider(),

            # タスク入力エリア
            rx.hstack(
                rx.input(
                    placeholder="新しいタスクを入力...",
                    on_change=State.set_new_item,
                    value=State.new_item,
                ),
                rx.button("追加", on_click=State.add_item, color_scheme="indigo"),
                width="100%",
            ),

            # タスク一覧エリア
            rx.vstack(
                rx.foreach(
                    State.items,
                    lambda item: rx.card(
                        rx.hstack(
                            rx.text(item, flex_grow="1"),
                            rx.button(
                                "削除", 
                                on_click=lambda: State.delete_item(item), 
                                color_scheme="red", 
                                size="1"
                            ),
                            width="100%",
                            align="center",
                        ),
                        width="100%",
                    )
                ),
                width="100%",
                spacing="2",
            ),

            spacing="4",
            style={"max_width": "450px", "width": "100%", "padding": "2rem"}
        ),
        width="100%",
        height="100vh",
        background_color="var(--gray-2)",
    )


app = rx.App()
app.add_page(index)