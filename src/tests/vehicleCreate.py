from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# Inicializar el WebDriver (en este caso se usa Chrome)
driver = webdriver.Chrome()


# Navegar a la URL inicial
driver.get("http://localhost:3001")

# Esperar unos segundos a que la página cargue completamente
time.sleep(2)

# Encontrar el enlace 'Iniciar Sesión' y hacer clic
iniciar_sesion_link = driver.find_element(By.XPATH, "//a[text()='Iniciar Sesión']")
iniciar_sesion_link.click()

# Esperar a que la página cambie (esperar 3 segundos para la redirección)
time.sleep(2)

# Ahora estamos en la página de login, encontrar los campos de entrada para el correo y la contraseña
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")

# Llenar los campos con las credenciales
email_input.send_keys("maria@example.com")
password_input.send_keys("password123")

# Encontrar el botón de 'Iniciar Sesión' y hacer clic
login_button = driver.find_element(By.XPATH, "//button[text()='Iniciar Sesión']")
login_button.click()

# Esperar a que la página de inicio cargue después de iniciar sesión
time.sleep(3)

# Esperar hasta que el enlace con href="/dashboard/cars/new" esté visible
crear_carros_enlace = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//a[@href='/dashboard/cars/new']")
    )
)

# Hacer clic en el enlace "Crear"
crear_carros_enlace.click()

time.sleep(3)

# Parámetros a ingresar
marca = "Chevrolet"
modelo = "Sentra"
imagen = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCWkKh4HDY6Lk6iP44J72k0c6bSK8h3uZmQQ&s"
matricula = "TBI-5015"
ano = "2013"
estado = "available"  # Disponible
costo_diario = "80"
tipo_vehiculo = "Personal"

marcaEditar = "Nissan"
modeloEditar = "Sentrassss"
imagenEditar = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCWkKh4HDY6Lk6iP44J72k0c6bSK8h3uZmQQ&s"
matriculaEditar = "TBI-3015"
anoEditar = "2000"
estadoEditar = "available"  # Disponible
costo_diario= "80"

# Coloca el parámetro "Marca"
marca_input = driver.find_element(By.NAME, "brand")
marca_input.send_keys(marca)
time.sleep(1)  # Espera 1 segundo

# Coloca el parámetro "Modelo"
modelo_input = driver.find_element(By.NAME, "model")
modelo_input.send_keys(modelo)
time.sleep(1)

# Coloca el parámetro "Imagen"
imagen_input = driver.find_element(By.NAME, "image")
imagen_input.send_keys(imagen)
time.sleep(1)

# Coloca el parámetro "Matricula"
matricula_input = driver.find_element(By.NAME, "license_plate")
matricula_input.send_keys(matricula)
time.sleep(1)

# Coloca el parámetro "Año"
ano_input = driver.find_element(By.NAME, "year")
ano_input.send_keys(ano)
time.sleep(1)

# Coloca el parámetro "Tipo de vehiculo"
tipo_vehiculo_input = driver.find_element(By.NAME, "vehicle_type")
tipo_vehiculo_input.send_keys("Sedan")  # Aquí puedes modificar según el tipo de vehículo
time.sleep(1)

# Coloca el costo diario
driver.find_element(By.NAME, "daily_rate").send_keys(costo_diario)

time.sleep(20)

# Envía el formulario
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

# Envía el formulario para crear el vehículo
crear_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
crear_btn.click()

# Espera 3 segundos para asegurarse de que la solicitud se haya enviado
time.sleep(3)

lista_btn = driver.find_element(By.XPATH, "//a[@href='/dashboard/cars/view']")
lista_btn.click()

time.sleep(3)

# Encontrar el botón de "Editar" y hacer clic
# Seleccionar el botón de edición por la clase del SVG
editar_btn = driver.find_element(By.XPATH, "//svg[contains(@class, 'lucide-pencil')]")
editar_btn.click()
time.sleep(2)

# Coloca el parámetro "Marca"
marca_input = driver.find_element(By.NAME, "bran")
marca_input.send_keys(marcaEditar)
time.sleep(1)  # Espera 1 segundo

# Coloca el parámetro "Modelo"
modelo_input = driver.find_element(By.NAME, "model")
modelo_input.send_keys(modeloEditar)
time.sleep(1)

# Coloca el parámetro "Imagen"
imagen_input = driver.find_element(By.NAME, "image")
imagen_input.send_keys(imagenEditar)
time.sleep(1)

# Coloca el parámetro "Matricula"
matricula_input = driver.find_element(By.NAME, "license_plate")
matricula_input.send_keys(matriculaEditar)
time.sleep(1)

# Coloca el parámetro "Año"
ano_input = driver.find_element(By.NAME, "year")
ano_input.send_keys(anoEditar)
time.sleep(1)

# Coloca el parámetro "Tipo de vehiculo"
tipo_vehiculo_input = driver.find_element(By.NAME, "vehicle_type")
tipo_vehiculo_input.send_keys("Personal")
time.sleep(1)

# Coloca el parámetro "Estado" (Disponible)
estado_input = driver.find_element(By.XPATH, "//span[text()='Selecciona el estado']")
driver.execute_script("arguments[0].scrollIntoView();", estado_input)  # Desplazar al elemento
estado_input.click()
time.sleep(1)

# Selecciona "Disponible" del dropdown
estado_disponible = driver.find_element(By.XPATH, "//option[@value='available']")
estado_disponible.click()
time.sleep(1)

# Coloca el parámetro "Costo diario"
costo_input = driver.find_element(By.NAME, "daily_rate")
costo_input.send_keys(costo_diario)
time.sleep(1)

editar_btn = driver.find_element(By.XPATH, "//button[text()='Actualizar']")
editar_btn.click()


# Encontrar el botón de "Eliminar" y hacer clic
eliminar_btn = driver.find_element(By.XPATH, "//svg[contains(@class, 'lucide-trash2')]")
eliminar_btn.click()


search_btn = driver.find_element(By.XPATH, "//a[@href='/dashboard/cars/information']")
search_btn.click()


# Esperar a que los filtros estén visibles (esperamos que el formulario de filtros esté disponible)
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h1[text()='Filtros']"))
)

# Seleccionar la opción de "10.00" para el filtro "Selecciona un valor mínimo"
min_price_10 = driver.find_element(By.XPATH, "//input[@name='min_price' and @value='10.00']")
min_price_10.click()

# Seleccionar la opción de "100.00" para el filtro "Selecciona un valor máximo"
max_price_100 = driver.find_element(By.XPATH, "//input[@name='max_price' and @value='100.00']")
max_price_100.click()

# Esperar un poco para verificar que se seleccionaron correctamente
time.sleep(2)

# Hacer clic en el botón "Limpiar Filtro"
limpiar_filtro_button = driver.find_element(By.XPATH, "//button[text()='Limpiar Filtro']")
limpiar_filtro_button.click()

# Esperar 3 segundos para asegurarse de que el filtro se ha limpiado
time.sleep(3)

# Cerrar el navegador
driver.quit()



