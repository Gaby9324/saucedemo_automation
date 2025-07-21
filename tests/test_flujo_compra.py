import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_complete_purchase(setup: WebDriver):
    driver = setup

    # 1. Login
    driver.get("https://saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Añadir productos al carrito
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_item"))
    )
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    for item in items[:2]:
        item.find_element(By.CLASS_NAME, "btn_inventory").click()

    # 3. Ir al carrito
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 4. Checkout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # 5. Completar formulario
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    ).send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # 6. Verificar que estamos en la página de resumen
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_info"))
    )

    # 7. Finalizar compra
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()

    # Verificación final
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "complete-header"), "Thank you for your order!")
    )
