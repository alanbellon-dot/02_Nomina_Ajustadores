import time
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.recuperaciones_page import RecuperacionesPage

def run():
    print("=== 🤖 BOT DE NÓMINA - ASEGURADORA DIGITAL ===")
    print("¿Qué proceso deseas ejecutar hoy?")
    print("1. Aprobar recuperación/recuperaciones")
    print("2. Rechazar recuperación/recuperaciones")
    print("3. Aprobar recuperación/recuperaciones rechazada(s)")
    print("4. Autorización en nómina individual")
    print("5. Nómina Autorizados (en proceso)")
    print("6. Historial (en proceso)")
    
    opcion = input("\nIngresa el número de tu elección (1-6): ").strip()
    
    if opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("❌ Opción no válida. Cerrando el bot.")
        return

    # --- INICIO DEL NAVEGADOR ---
    with sync_playwright() as p:
        print("\nLanzando navegador...")
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        context = browser.new_context(no_viewport=True)
        page = context.new_page()

        login_p = LoginPage(page)
        recuperaciones_p = RecuperacionesPage(page)

        # --- LOGIN ---
        try:
            print("\n--- Iniciando Sesión ---")
            login_p.navigate()
            login_p.login("DEVBANORTE", "12345678")
            page.wait_for_url(lambda url: "/inicio" in url or "/panel-control" in url, timeout=30000)
            print("✅ Login exitoso.")
        except Exception as e:
            print(f"❌ Error fatal en Login: {e}")
            return

        # --- EJECUCIÓN LÓGICA SEGÚN LA OPCIÓN ---
        try:
            if opcion == "1":
                print("\n--- Ejecutando: 1. Aprobar recuperación ---")
                recuperaciones_p.navegar_al_modulo()
                recuperaciones_p.buscar_y_ver_detalle("Vanessa Enriquez García")
                
            elif opcion == "2":
                print("\n--- Ejecutando: 2. Rechazar recuperación ---")
                recuperaciones_p.navegar_al_modulo()
                recuperaciones_p.buscar_y_rechazar("Vanessa Enriquez García")
                
            elif opcion == "3":
                print("\n--- Ejecutando: 3. Aprobar recuperación rechazada ---")
                recuperaciones_p.navegar_a_recuperaciones_rechazadas()
                recuperaciones_p.buscar_y_ver_detalle("Vanessa Enriquez García")
                
            elif opcion == "4":
                print("\n--- Ejecutando: 4. Autorización en nómina individual ---")
                recuperaciones_p.navegar_a_nomina()
                recuperaciones_p.buscar_y_autorizar_nomina("Vanessa Enriquez García")
                
            elif opcion == "5":
                print("\n--- Ejecutando: 5. Nómina Autorizados (en proceso) ---")
                recuperaciones_p.navegar_a_autorizados()
                recuperaciones_p.buscar_basico("Vanessa Enriquez García")

            elif opcion == "6":
                print("\n--- Ejecutando: 6. Historial (en proceso) ---")
                recuperaciones_p.navegar_a_historial()
                recuperaciones_p.buscar_basico("Vanessa Enriquez García")

            print("\n✅ Proceso completado con éxito.")
            time.sleep(5)

        except Exception as e:
            print(f"🔥 Error en el flujo: {e}")

        print("\n=== CERRANDO NAVEGADOR ===")
        browser.close()

if __name__ == "__main__":
    run()