import mesop as me
import mesop.labs as mel
import imagen_func as img
import flux_func as flx
import base64

#CLASS DEFINITIONS
@me.stateclass
class State:
  imagen_input: str
  imagen_output: str
  imagen_textarea_key: int

@me.stateclass
class fluxState:
  flux_input: str
  flux_output: str
  flux_textarea_key: int

#STATE CHANGE FUNCTIONS
def on_input(e: me.InputEvent):
    state = me.state(State)
    state.imagen_input = e.value

def on_click_tti(e: me.ClickEvent):
  me.navigate("/text_to_image")

def on_click_ttv(e: me.ClickEvent):
  me.navigate("/text_to_video")

def on_click_clear_imagen(e: me.ClickEvent):
    state = me.state(State)
    state.imagen_input = ""
    state.imagen_output = ""
    state.imagen_textarea_key += 1

def on_click_generate_imagen(e: me.ClickEvent):
    state = me.state(State)
    state.imagen_output = generate_imagen(state.imagen_input)

def on_click_clear_flux(e: me.ClickEvent):
    state = me.state(fluxState)
    state.flux_input = ""
    state.flux_output = ""
    state.flux_textarea_key += 1

def on_click_generate_flux(e: me.ClickEvent):
    state = me.state(fluxState)
    state.flux_output = generate_flux(state.flux_input)

#GENERATION FUNCTIONS


def generate_imagen(prompt: str):

    img.generateImage_imagen(prompt)

    with open("./imagenGenerated/image.jpg", "rb") as f:
        image_data = f.read()
        encoded_image = base64.b64encode(image_data).decode("utf-8")
        

    return f"data:image/jpeg;base64,{encoded_image}"

def generate_flux(prompt:str):
    
    flx.generatedImage_Flux(prompt)

    with open("./fluxGenerated/fluxImage.png", "rb") as f:
        image_data = f.read()
        encoded_image = base64.b64encode(image_data).decode("utf-8")
    
    return f"data:image/jpeg;base64,{encoded_image}"

@me.page(path="/")

#TEXT TO IMAGE

@me.page(path="/text_to_image",
)

def app():

    is_mobile = me.viewport_size().width < 640 
    
    with me.box(style=me.Style(display="flex", flex_direction="row", gap=12)):
        me.button("Text to Image", on_click=on_click_tti)
        me.button("Text to Video", on_click=on_click_ttv)
    
    #CONTAINER 
    with me.box(style=me.Style(display="flex",flex_direction="column")):

        #IMAGEN
        with me.box(
        style=me.Style(
        background="#f0f4f8",
        height="100%",
        )
        ):
            with me.box(
            style=me.Style(
                background="#f0f4f8",
                padding=me.Padding(top=24, left=24, right=24, bottom=24),
                display="flex",
                flex_direction="column",
            )
            ):
                with me.box(
                    style=me.Style(
                        align_self="center",
                        padding=me.Padding(top=10, bottom=5)
                    )
                ):
                    me.text("Imagen 3", type="headline-3")
                with me.box(
                    style=me.Style(
                        margin=me.Margin(left="auto", right="auto"),
                        width="min(1024px, 100%)",
                        gap="24px",
                        flex_grow=1,
                        display="flex",
                        flex_wrap="wrap",
                    )
                ):
                    box_style = me.Style(
                    flex_basis="max(200px, calc(50% - 48px))",
                    background="#fff",
                    border_radius=12,
                    box_shadow=(
                        "0 3px 1px -2px #0003, 0 2px 2px #00000024, 0 1px 5px #0000001f"
                    ),
                    padding=me.Padding(top=16, left=16, right=16, bottom=16),
                    display="flex",
                    flex_direction="column",
                    )

                    with me.box(style=box_style):
                        me.text("Input", style=me.Style(font_weight=500))
                        me.box(style=me.Style(height=16))
                        me.textarea(
                            key=str(me.state(State).imagen_textarea_key),
                            on_input=on_input,
                            rows=5,
                            autosize=True,
                            max_rows=15,
                            style=me.Style(width="100%"),
                        )
                        me.box(style=me.Style(height=50))
                        with me.box(
                            style=me.Style(display="flex", justify_content="space-between")
                        ):
                            me.button(
                            "Clear",
                            color="primary",
                            type="stroked",
                            on_click=on_click_clear_imagen,
                            )
                            me.button(
                            "Generate",
                            color="primary",
                            type="flat",
                            on_click=on_click_generate_imagen,
                            )
                    with me.box(style=box_style):
                        me.text("Output", style=me.Style(font_weight=500))
                        if me.state(State).imagen_output:
                            with me.box(
                            style=me.Style(
                                display="grid",
                                justify_content="center",
                                justify_items="center",
                                max_height=50,
                            )
                            ):
                                me.image(
                                    src=me.state(State).imagen_output,
                                    style=me.Style(max_height="75%",width="100%", margin=me.Margin(top=10)),
                                )

        #FLUX                    
        with me.box(
        style=me.Style(
        background="#f0f4f8",
        height="100%",
        )
        ):
            with me.box(
            style=me.Style(
                background="#f0f4f8",
                padding=me.Padding(top=24, left=24, right=24, bottom=24),
                display="flex",
                flex_direction="column",
            )
            ):
                with me.box(
                    style=me.Style(
                        align_self="center",
                        padding=me.Padding(top=10, bottom=5)
                    )
                ):
                    me.text("Flux", type="headline-3")
                with me.box(
                    style=me.Style(
                        margin=me.Margin(left="auto", right="auto"),
                        width="min(1024px, 100%)",
                        gap="24px",
                        flex_grow=1,
                        display="flex",
                        flex_wrap="wrap",
                    )
                ):
                    box_style = me.Style(
                    flex_basis="max(480px, calc(50% - 48px))",
                    background="#fff",
                    border_radius=12,
                    box_shadow=(
                        "0 3px 1px -2px #0003, 0 2px 2px #00000024, 0 1px 5px #0000001f"
                    ),
                    padding=me.Padding(top=16, left=16, right=16, bottom=16),
                    display="flex",
                    flex_direction="column",
                    )

                    with me.box(style=box_style):
                        me.text("Input", style=me.Style(font_weight=500))
                        me.box(style=me.Style(height=16))
                        me.textarea(
                            key=str(me.state(fluxState).flux_textarea_key),
                            on_input=on_input,
                            rows=5,
                            autosize=True,
                            max_rows=7,
                            style=me.Style(width="100%", height="100%"),
                        )
                        me.box(style=me.Style(height=50))
                        with me.box(
                            style=me.Style(display="flex", justify_content="space-between")
                        ):
                            me.button(
                            "Clear",
                            color="primary",
                            type="stroked",
                            on_click=on_click_clear_flux,
                            )
                            me.button(
                            "Generate",
                            color="primary",
                            type="flat",
                            on_click=on_click_generate_flux,
                            )
                    with me.box(style=box_style):
                        me.text("Output", style=me.Style(font_weight=500))
                        if me.state(fluxState).flux_output:
                            with me.box(
                            style=me.Style(
                                display="grid",
                                justify_content="center",
                                justify_items="center",
                                max_height=50,
                            )
                            ):
                                me.image(
                                    src=me.state(fluxState).flux_output,
                                    style=me.Style(max_height="80%",width="100%", margin=me.Margin(top=10)),
                                )


#TEXT TO VIDEO

@me.page(path="/text_to_video",
)

def app():
    with me.box(style=me.Style(display="flex", flex_direction="row", gap=12)):
        me.button("Text to Image", on_click=on_click_tti)
        me.button("Text to Video", on_click=on_click_ttv)
    

    

