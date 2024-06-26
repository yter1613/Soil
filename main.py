import tkinter as tk

# Функция для получения свойств типа грунта | Function to get soil type properties
def get_soil_type_properties(choice):
    properties = {
        1: (0.73, 12.2, 0.32),
        2: (0.46, 7.2, 0.10),
        3: (0.53, 9.7, -0.36)
    }
    return properties.get(choice)

# Функция для получения параметров ввода | Function to get input parameters
def get_input_parameters():
    try:
        return (
            float(particle_density_var.get()),
            float(norm_density_var.get()),
            float(natural_moisture_var.get())
        )
    except ValueError:
        result_text.set("Неверный ввод. | Invalid input.")
        return None, None, None

# Функция для выполнения расчетов и отображения результатов | Function to perform calculations and display results
def calculate_and_display_results():
    choice = soil_type_choice.get()
    props = get_soil_type_properties(choice)

    if not props:
        result_text.set("Ошибка. | Error.")
        return

    particle_density, norm_density, natural_moisture = get_input_parameters()
    if particle_density is None:
        return

    porosity_coefficient, plasticity_number, flow_index = props

    # Вычисления | Calculations
    skeleton_density = norm_density / (1 + natural_moisture / 100)
    porosity_value = 1 - (skeleton_density / particle_density)
    porosity_saturation = porosity_coefficient / particle_density * 100
    moisture_content_value = natural_moisture / porosity_saturation
    specific_weight = norm_density * 10
    skeleton_specific_weight = skeleton_density * 10
    specific_weight_with_water_effect = (particle_density - 1) / (1 + porosity_coefficient) * 10
    specific_weight_at_full_saturation = skeleton_specific_weight * (1 + porosity_saturation / 100)

    # Отображение результатов | Display results
    result = (
        f"Плотность скелета грунта: {skeleton_density:.2f}\n"
        f"Пористость грунта: {porosity_value:.2f}\n"
        f"Влажность при полном водонасыщении: {porosity_saturation:.2f}\n"
        f"Степень влажности: {moisture_content_value:.2f}\n"
        f"Удельный вес грунта: {specific_weight:.2f}\n"
        f"Удельный вес скелета грунта: {skeleton_specific_weight:.2f}\n"
        f"Удельный вес с учетом взвешивающего действия воды: {specific_weight_with_water_effect:.2f}\n"
        f"Удельный вес при полном водонасыщении: {specific_weight_at_full_saturation:.2f}\n"
    )
    result_text.set(result)

# Основная функция для создания GUI и запуска программы | Main function to create GUI and run the program
def main():
    root = tk.Tk()
    root.title("Расчет геотехнических свойств | Geotechnical Properties Calculation")

    global soil_type_choice, particle_density_var, norm_density_var, natural_moisture_var, result_text
    soil_type_choice = tk.IntVar()
    particle_density_var = tk.StringVar()
    norm_density_var = tk.StringVar()
    natural_moisture_var = tk.StringVar()
    result_text = tk.StringVar()

    soil_types = ["Суглинок тугопластичный | Suglinok tugoplasticniy", "Суглинок пластичный | Suglinok plasticniy", "Суглинок твердый | Suglinok tverdiy"]
    for i, soil in enumerate(soil_types, 1):
        tk.Radiobutton(root, text=soil, variable=soil_type_choice, value=i).pack()

    labels_and_vars = [
        ("Плотность частиц грунта (г/см3) | Particle density (g/cm3):", particle_density_var),
        ("Нормативная плотность грунта (г/см3) | Normative soil density (g/cm3):", norm_density_var),
        ("Природная влажность грунта (%) | Natural soil moisture (%):", natural_moisture_var)
    ]

    for text, var in labels_and_vars:
        tk.Label(root, text=text).pack()
        tk.Entry(root, textvariable=var).pack()

    tk.Button(root, text="Рассчитать | Calculate", command=calculate_and_display_results).pack()
    tk.Label(root, textvariable=result_text).pack()

    # Создание таблицы | Create table
    table = tk.Frame(root)
    table.pack(side="top", padx=10, pady=10)

    # Заголовки столбцов таблицы | Table column headers
    cols = ["ИГЭ 1", "Столбец 2 | Column 2", "Столбец 3 | Column 3"]
    for i, col in enumerate(cols):
        tk.Label(table, text=col, width=15).grid(row=0, column=i)

    # Выпадающие списки в первом столбце | Dropdown lists in the first column
    rows = 20
    for i in range(rows):
        var = tk.StringVar()
        choices = ["ИГЭ 1", "ИГЭ 2", "ИГЭ 3", "ИГЭ 4"]
        var.set(choices[0])
        tk.OptionMenu(table, var, *choices).grid(row=i+1, column=0)

    # Поля ввода для остальных столбцов | Entry fields for the other columns
    for i in range(rows):
        for j in range(1, 3):
            tk.Entry(table, width=15).grid(row=i+1, column=j)

    root.mainloop()

if __name__ == "__main__":
    main()
