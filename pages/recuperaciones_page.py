from playwright.sync_api import Page

class RecuperacionesPage:
    def __init__(self, page: Page):
        self.page = page

        # --- NAVEGACIÓN ---
        self.icon_menu = page.locator("mat-icon:text('menu')").first
        self.btn_nomina_ajustadores = page.locator("span.menu-title", has_text="Nómina ajustadores").first
        
        # Submenús 
        self.btn_autorizados_menu = page.locator("span.menu-title:text-is('Autorizados')").first
        self.btn_nomina_menu = page.locator("span.menu-title:text-is('Nómina')").first
        self.btn_recuperaciones = page.locator("span.menu-title", has_text="Recuperaciones").first
        self.btn_recuperaciones_rechazadas = page.locator("span.menu-title", has_text="Recuperaciones rechazadas").first
        # NUEVO: Submenú Historial
        self.btn_historial_menu = page.locator("span.menu-title:text-is('Historial')").first

        # --- SELECTORES BÚSQUEDA (Reutilizables en todas las pantallas) ---
        self.input_ajustador = page.locator("input[formcontrolname='idAjustador']")
        self.btn_calendario = page.locator("mat-datepicker-toggle button")
        self.dia_1 = page.locator("div.mat-calendar-body-cell-content", has_text="1").first
        self.btn_buscar = page.locator("button", has_text="Buscar")
        
        # --- SELECTORES GENERALES ---
        self.btn_ver_detalle_general = page.locator("text=Ver detalle").first
        
        # --- BOTONES DE APROBAR / RECHAZAR ---
        self.btn_aprobar = page.locator("span", has_text="Aprobar").first
        self.btn_rechazar = page.locator("span", has_text="Rechazar").first
        
        # --- NUEVOS SELECTORES PARA EL MOTIVO DE RECHAZO ---
        self.textarea_motivo = page.locator("textarea[data-placeholder='Capture el motivo.']").first
        self.btn_enviar_rechazo = page.locator("button[status='primary']", has_text="Enviar").last
        
        self.btn_autorizar = page.locator("button", has_text="Autorizar").first

        # --- SELECTORES PARA "AUTORIZADOS" ---
        self.btn_enviar_opciones = page.locator("button[aria-disabled='false']").filter(has_text="Enviar").filter(has=page.locator("nb-icon[icon='options-2-outline']")).first
        self.btn_enviar_navegacion = page.locator("button").filter(has=page.locator("nb-icon[icon='navigation-2-outline']")).last
        self.checkbox_elemento = page.locator("mat-checkbox").last
        self.btn_enviar_notificacion = page.locator("button[status='primary']", has_text="Enviar").last
        self.icon_clear = page.locator("mat-icon:text-is('clear')").last

        # Botones de las alertas emergentes (SweetAlert2)
        self.btn_confirmar_alerta = page.locator("button.swal2-confirm", has_text="Confirmar")
        self.btn_aceptar_alerta = page.locator("button.swal2-confirm", has_text="Aceptar")

    # === HELPER: ESCUDO CONTRA ALERTAS DE BIENVENIDA ===
    def _cerrar_alerta_bienvenida(self):
        try:
            if self.btn_aceptar_alerta.is_visible(timeout=2000):
                print("⚠️ Alerta detectada. Dando clic en 'Aceptar'...")
                self.btn_aceptar_alerta.click(force=True)
                self.page.wait_for_timeout(1000)
        except:
            pass 

    # === RUTAS DE NAVEGACIÓN ===
    def navegar_a_autorizados(self):
        print("Abriendo el Menú principal (Icono 3 rayitas)...")
        self.icon_menu.click()
        self.page.wait_for_timeout(500)
        print("Desplegando 'Nómina ajustadores'...")
        self.btn_nomina_ajustadores.click()
        self.page.wait_for_timeout(500) 
        print("Seleccionando submenú 'Autorizados'...")
        self.btn_autorizados_menu.click()
        self.page.wait_for_timeout(2000)
        self._cerrar_alerta_bienvenida() 

    def navegar_a_historial(self):
        print("Abriendo el Menú principal (Icono 3 rayitas)...")
        self.icon_menu.click()
        self.page.wait_for_timeout(500)
        print("Desplegando 'Nómina ajustadores'...")
        self.btn_nomina_ajustadores.click()
        self.page.wait_for_timeout(500) 
        print("Seleccionando submenú 'Historial'...")
        self.btn_historial_menu.click()
        self.page.wait_for_timeout(2000)
        self._cerrar_alerta_bienvenida() 

    def navegar_al_modulo(self):
        print("Abriendo el Menú principal (Icono 3 rayitas)...")
        self.icon_menu.click()
        self.page.wait_for_timeout(500)
        print("Desplegando 'Nómina ajustadores'...")
        self.btn_nomina_ajustadores.click()
        self.page.wait_for_timeout(500) 
        print("Seleccionando 'Recuperaciones'...")
        self.btn_recuperaciones.click()
        self.page.wait_for_timeout(2000)
        self._cerrar_alerta_bienvenida() 

    def navegar_a_recuperaciones_rechazadas(self):
        print("Abriendo el Menú principal (Icono 3 rayitas)...")
        self.icon_menu.click()
        self.page.wait_for_timeout(500)
        print("Desplegando 'Nómina ajustadores'...")
        self.btn_nomina_ajustadores.click()
        self.page.wait_for_timeout(500) 
        print("Seleccionando 'Recuperaciones rechazadas'...")
        self.btn_recuperaciones_rechazadas.click()
        self.page.wait_for_timeout(2000)
        self._cerrar_alerta_bienvenida() 

    def navegar_a_nomina(self):
        print("Abriendo el Menú principal (Icono 3 rayitas)...")
        self.icon_menu.click()
        self.page.wait_for_timeout(500)
        print("Desplegando menú 'Nómina ajustadores'...")
        self.btn_nomina_ajustadores.click()
        self.page.wait_for_timeout(500) 
        print("Seleccionando el submenú exacto 'Nómina'...")
        self.btn_nomina_menu.click()
        self.page.wait_for_timeout(2000)
        self._cerrar_alerta_bienvenida()

    # === FUNCIONES DE PROCESAMIENTO ===
    def buscar_basico(self, nombre_ajustador="Vanessa Enriquez García"):
        """NUEVA FUNCIÓN: Solo busca y se detiene (Para opciones 5 y 6)"""
        print(f"Ingresando el nombre del ajustador: {nombre_ajustador}...")
        self.input_ajustador.click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        self.input_ajustador.press_sequentially(nombre_ajustador, delay=10)
        try:
            self.page.wait_for_selector("mat-option", timeout=5000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(200)
            self.page.keyboard.press("Enter")
        except:
            self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)

        print("Abriendo calendario...")
        self.btn_calendario.click()
        self.page.wait_for_timeout(500) 
        self.dia_1.click(force=True)
        self.page.keyboard.press("Escape") 
        self.page.wait_for_timeout(500)

        print("Dando clic en Buscar...")
        self.btn_buscar.click()
        self.page.wait_for_timeout(2000)
        print("✅ Búsqueda completada.")

    def buscar_y_enviar_autorizados(self, nombre_ajustador="Vanessa Enriquez García"):
        print(f"Buscando al ajustador en Autorizados: {nombre_ajustador}...")
        self.input_ajustador.click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        self.input_ajustador.press_sequentially(nombre_ajustador, delay=10)
        
        try:
            self.page.wait_for_selector("mat-option", timeout=5000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(200)
            self.page.keyboard.press("Enter")
        except:
            self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)

        self.btn_calendario.click()
        self.page.wait_for_timeout(500) 
        self.dia_1.click(force=True)
        self.page.keyboard.press("Escape") 
        self.page.wait_for_timeout(500)

        self.btn_buscar.click()
        self.page.wait_for_timeout(2000)

        self.btn_ver_detalle_general.click()
        self.page.wait_for_timeout(3000) 

        fila_tiempo_arribo = self.page.locator("tr").filter(has_text="Tiempo de Arribo").first
        fila_tiempo_arribo.scroll_into_view_if_needed()
        self.page.wait_for_timeout(1000)
        
        btn_enviar_arribo = fila_tiempo_arribo.locator("button[aria-disabled='false']").filter(has_text="Enviar").first
        btn_enviar_arribo.click()
        
        self.page.wait_for_selector("mat-checkbox", state="visible", timeout=10000)
        self.checkbox_elemento.click(force=True)
        self.page.wait_for_timeout(1500) 

        self.btn_enviar_navegacion.scroll_into_view_if_needed()
        self.btn_enviar_navegacion.click(force=True)
        self.page.wait_for_timeout(1500) 
        
        self.btn_enviar_notificacion.click(force=True)
        self.page.wait_for_timeout(2000)
        
        try:
            if self.btn_aceptar_alerta.is_visible():
                self.btn_aceptar_alerta.click(force=True)
                self.page.wait_for_timeout(1000)
        except:
            pass

        self.icon_clear.click(force=True)
        self.page.wait_for_timeout(1000)

    def buscar_y_ver_detalle(self, nombre_ajustador="Vanessa Enriquez García"):
        print(f"Buscando al ajustador (Para Aprobar): {nombre_ajustador}...")
        self.input_ajustador.click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        self.input_ajustador.press_sequentially(nombre_ajustador, delay=10)
        try:
            self.page.wait_for_selector("mat-option", timeout=5000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(200)
            self.page.keyboard.press("Enter")
        except:
            self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)

        self.btn_calendario.click()
        self.page.wait_for_timeout(500) 
        self.dia_1.click(force=True)
        self.page.keyboard.press("Escape") 
        self.page.wait_for_timeout(500)

        self.btn_buscar.click()
        self.page.wait_for_timeout(2000)

        self.btn_ver_detalle_general.click()
        self.page.wait_for_timeout(3000) 

        print("Dando clic en APROBAR a la primera fila...")
        self.btn_aprobar.click()
        self.page.wait_for_timeout(500)
        self.btn_confirmar_alerta.click()
        self.page.wait_for_timeout(2000)
        try:
            if self.btn_aceptar_alerta.is_visible():
                self.btn_aceptar_alerta.click()
        except:
            pass
        self.page.wait_for_timeout(1000)
        
        print("Cerrando la ventana de Detalles...")
        self.icon_clear.click(force=True)
        self.page.wait_for_timeout(1000)
        print("✅ ¡Recuperación aprobada correctamente y ventana cerrada!")

    def buscar_y_rechazar(self, nombre_ajustador="Vanessa Enriquez García"):
        print(f"Buscando al ajustador (Para Rechazar): {nombre_ajustador}...")
        self.input_ajustador.click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        self.input_ajustador.press_sequentially(nombre_ajustador, delay=10)
        try:
            self.page.wait_for_selector("mat-option", timeout=5000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(200)
            self.page.keyboard.press("Enter")
        except:
            self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)

        self.btn_calendario.click()
        self.page.wait_for_timeout(500) 
        self.dia_1.click(force=True)
        self.page.keyboard.press("Escape") 
        self.page.wait_for_timeout(500)

        self.btn_buscar.click()
        self.page.wait_for_timeout(2000)

        self.btn_ver_detalle_general.click()
        self.page.wait_for_timeout(3000) 
        
        print("Dando clic en RECHAZAR a la primera fila...")
        self.btn_rechazar.click()
        self.page.wait_for_timeout(1000)
        
        print("Confirmando la alerta de rechazo...")
        self.btn_confirmar_alerta.click(force=True)
        self.page.wait_for_timeout(1500)
        
        print("Escribiendo el motivo del rechazo...")
        self.textarea_motivo.fill("Prueba Rechazo")
        self.page.wait_for_timeout(500)
        
        print("Dando clic en Enviar motivo...")
        self.btn_enviar_rechazo.click(force=True)
        self.page.wait_for_timeout(2000)
        
        print("Esperando confirmación de éxito...")
        try:
            if self.btn_confirmar_alerta.is_visible():
                self.btn_confirmar_alerta.click()
                self.page.wait_for_timeout(2000)
            if self.btn_aceptar_alerta.is_visible():
                self.btn_aceptar_alerta.click()
        except:
            pass
        self.page.wait_for_timeout(1000)
        
        print("Cerrando la ventana de Detalles...")
        self.icon_clear.click(force=True)
        self.page.wait_for_timeout(1000)
        print("✅ ¡Recuperación rechazada correctamente y ventana cerrada!")

    def buscar_y_autorizar_nomina(self, nombre_ajustador="Vanessa Enriquez García"):
        print(f"Buscando al ajustador en Nómina: {nombre_ajustador}...")
        self.input_ajustador.click()
        self.page.keyboard.press("Control+A")
        self.page.keyboard.press("Backspace")
        self.input_ajustador.press_sequentially(nombre_ajustador, delay=10)
        try:
            self.page.wait_for_selector("mat-option", timeout=5000)
            self.page.keyboard.press("ArrowDown")
            self.page.wait_for_timeout(200)
            self.page.keyboard.press("Enter")
        except:
            self.page.keyboard.press("Enter")
        self.page.wait_for_timeout(2000)

        self.btn_calendario.click()
        self.page.wait_for_timeout(500) 
        self.dia_1.click(force=True)
        self.page.keyboard.press("Escape") 
        self.page.wait_for_timeout(500)

        self.btn_buscar.click()
        self.page.wait_for_timeout(2000)

        self.btn_ver_detalle_general.click()
        self.page.wait_for_timeout(3000) 

        self.btn_autorizar.scroll_into_view_if_needed()
        self.page.wait_for_timeout(1000)
        try:
            self.btn_autorizar.click(force=True, timeout=5000)
        except Exception as e:
            print("❌ ERROR: No se pudo hacer clic en 'Autorizar'. Asegúrate de que no esté 'disabled'.")
            raise e
        self.page.wait_for_timeout(1500)

        try:
            if self.btn_confirmar_alerta.is_visible():
                self.btn_confirmar_alerta.click()
                self.page.wait_for_timeout(2000)
            if self.btn_aceptar_alerta.is_visible():
                self.btn_aceptar_alerta.click()
        except:
            pass