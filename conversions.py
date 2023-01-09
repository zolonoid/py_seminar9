import temp2temp
import pypressure
import color_convert.color
import area_unit_conversion
import unitc
import conversion

print("Демонстрация нескольких библиотек для конвертации различных величин и данных.")

print("\nБиблиотека temp2temp для конвертации значений температуры:")
print("temp2temp.Celsius.to_kelvin(321)")
print(temp2temp.Celsius.to_kelvin(321))
print("temp2temp.Rankine.to_newton(321)")
print(temp2temp.Rankine.to_newton(321))

print("\nБиблиотека PyPressure для конвертации величин давления:")
print("pypressure.Pressure.patopsi(25.0)")
print(pypressure.Pressure.patopsi(25.0))
print("pypressure.Pressure.bartopa(50.0)")
print(pypressure.Pressure.bartopa(50.0))

print("\nБиблиотека color-convert для преобразования различных числовых значений в формат цвета RGB")
print("color_convert.color.hex_to_rgb('#fff000')")
print(color_convert.color.hex_to_rgb('#fff000'))
print("color_convert.color.ten_to_rgb(16711680)")
print(color_convert.color.ten_to_rgb(16711680))

print("\nБиблиотека area-unit-conversion для конвертации значений площади из одной системы единиц в другую:")
print("area_unit_conversion.convert('m2','ha',10000)")
print(area_unit_conversion.convert('m2','ha',10000))
print("area_unit_conversion.convert('ft2','m2',100)")
print(area_unit_conversion.convert('ft2','m2',100))

print("\nБиблиотека unitc для конвертации различных единиц измерения:")
print("unitc.unit_conversion(1, from_unit='kg', to_unit='lb')")
print(unitc.unit_conversion(1, from_unit='kg', to_unit='lb'))
print("unitc.unit_conversion('4 g/cm³', to_unit='lb/in³')")
print(unitc.unit_conversion('4 g/cm³', to_unit='lb/in³'))

print("\nБиблиотека conversion для преобразования строк в объекты Python:")
print("conversion.convert_bool('yes')")
print(conversion.convert_bool('yes'))
print("conversion.convert_delta('1h')")
print(conversion.convert_delta('1h'))