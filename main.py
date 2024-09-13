import flet as ft

def main(page: ft.Page):
    page.title = "Suma y Muestra Imagen"

    # Función para manejar el evento de clic del botón
    def button_clicked(e):
        try:
            num1 = float(input1.value)
            num2 = float(input2.value)
            result.value = f"Resultado: {num1 + num2}"
        except ValueError:
            result.value = "Por favor, ingresa números válidos."
        page.update()

    # Campos de entrada para los números
    input1 = ft.TextField(label="Número 1")
    input2 = ft.TextField(label="Número 2")

    # Botón para realizar la suma
    button = ft.ElevatedButton(text="Sumar", on_click=button_clicked)

    # Campo para mostrar el resultado
    result = ft.Text(value="Resultado: ")

    # Imagen a mostrar al final
    image = ft.Image(src="ruta/a/tu/imagen.jpg", width=200, height=200)

    # Añadir los controles a la página
    page.add(input1, input2, button, result, image)

ft.app(target=main)


ft.app(main)