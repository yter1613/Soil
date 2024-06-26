## Read Me

### Overview
This Python script calculates geotechnical properties of soil and provides a GUI interface for inputting data and displaying results. The program allows the user to select a soil type, input various parameters, and view the calculated properties such as skeleton density, porosity, and specific weights.

### Dependencies
- Python 3.x
- Tkinter (Python's standard GUI package)

### Files
- `main.py`: The main Python script containing the code for the GUI and calculations.

### How to Use
1. **Run the Script**:
   - Execute the script `main.py` using a Python interpreter.

2. **Select Soil Type**:
   - Choose the type of soil from the provided options: "Суглинок тугопластичный | Suglinok tugoplasticniy", "Суглинок пластичный | Suglinok plasticniy", "Суглинок твердый | Suglinok tverdiy".

3. **Enter Parameters**:
   - Input the following parameters in the provided fields:
     - **Particle density (g/cm3)**: Плотность частиц грунта (г/см3)
     - **Normative soil density (g/cm3)**: Нормативная плотность грунта (г/см3)
     - **Natural soil moisture (%)**: Природная влажность грунта (%)

4. **Calculate**:
   - Click the "Рассчитать | Calculate" button to perform the calculations.

5. **View Results**:
   - The results will be displayed in the application window, including:
     - Skeleton density
     - Porosity
     - Moisture at full saturation
     - Degree of moisture
     - Specific weight
     - Skeleton specific weight
     - Specific weight with water effect
     - Specific weight at full saturation

6. **Use the Table**:
   - The table allows for selection and entry of additional data, with options in the first column and entry fields in the remaining columns.

### Code Structure
- **Functions**:
  - `get_soil_type_properties(choice)`: Returns the properties for the selected soil type.
  - `get_input_parameters()`: Retrieves input parameters from the user.
  - `calculate_and_display_results()`: Performs calculations and updates the result display.

- **Main Function**:
  - `main()`: Initializes the GUI, sets up the interface elements, and runs the Tkinter main loop.

### Comments in Code
The code is commented in both Russian and English to explain the functionality of each part of the script.

### Example Execution
To run the script, use the following command in your terminal or command prompt:

```bash
python main.py
```

### Additional Information
- Ensure you have Python and Tkinter installed on your machine.
- Modify the `main.py` script as needed to adapt it to your specific requirements.

For any issues or further customization, refer to Python's Tkinter documentation and relevant resources.

## Read Me

### Обзор
Этот Python-скрипт вычисляет геотехнические свойства грунта и предоставляет графический интерфейс для ввода данных и отображения результатов. Программа позволяет пользователю выбрать тип грунта, ввести различные параметры и увидеть рассчитанные свойства, такие как плотность скелета, пористость и удельный вес.

### Зависимости
- Python 3.x
- Tkinter (стандартный пакет GUI для Python)

### Файлы
- `main.py`: Основной Python-скрипт, содержащий код для графического интерфейса и вычислений.

### Как использовать
1. **Запуск скрипта**:
   - Выполните скрипт `main.py` с помощью интерпретатора Python.

2. **Выбор типа грунта**:
   - Выберите тип грунта из предложенных вариантов: "Суглинок тугопластичный | Suglinok tugoplasticniy", "Суглинок пластичный | Suglinok plasticniy", "Суглинок твердый | Suglinok tverdiy".

3. **Ввод параметров**:
   - Введите следующие параметры в предоставленные поля:
     - **Плотность частиц грунта (г/см3)**: Particle density (g/cm3)
     - **Нормативная плотность грунта (г/см3)**: Normative soil density (g/cm3)
     - **Природная влажность грунта (%)**: Natural soil moisture (%)

4. **Расчет**:
   - Нажмите кнопку "Рассчитать | Calculate" для выполнения расчетов.

5. **Просмотр результатов**:
   - Результаты будут отображены в окне приложения, включая:
     - Плотность скелета
     - Пористость
     - Влажность при полном водонасыщении
     - Степень влажности
     - Удельный вес
     - Удельный вес скелета
     - Удельный вес с учетом взвешивающего действия воды
     - Удельный вес при полном водонасыщении

6. **Использование таблицы**:
   - Таблица позволяет выбирать и вводить дополнительные данные, с вариантами в первом столбце и полями ввода в остальных столбцах.

### Структура кода
- **Функции**:
  - `get_soil_type_properties(choice)`: Возвращает свойства для выбранного типа грунта.
  - `get_input_parameters()`: Получает параметры ввода от пользователя.
  - `calculate_and_display_results()`: Выполняет вычисления и обновляет отображение результатов.

- **Основная функция**:
  - `main()`: Инициализирует GUI, настраивает элементы интерфейса и запускает главный цикл Tkinter.

### Комментарии в коде
Код содержит комментарии на русском и английском языках для объяснения функциональности каждой части скрипта.

### Пример выполнения
Чтобы запустить скрипт, используйте следующую команду в терминале или командной строке:

```bash
python main.py
```

### Дополнительная информация
- Убедитесь, что Python и Tkinter установлены на вашем компьютере.
- При необходимости измените скрипт `main.py` для адаптации к вашим конкретным требованиям.

При возникновении проблем или для дальнейшей настройки, обратитесь к документации по Tkinter для Python и соответствующим ресурсам.# Soil
