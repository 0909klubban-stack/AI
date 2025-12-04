# OFFLINE-AI — SAFE DEFAULT + ALL FEATURES (OPT-IN)

---

## 🛡️ OFFLINE-AI – SAFE DEFAULT (STANDARDLÄGE)

Detta är den **rekommenderade standardkonfigurationen** av OFFLINE-AI.  
Alla avancerade, experimentella och potentiellt riskfyllda funktioner är:

> ❌ **AVSTÄNGDA SOM STANDARD**

Systemet är:

- ✅ 100% offline  
- ✅ Lokalt  
- ✅ Utan moln  
- ✅ Utan telemetri  
- ✅ Utan fjärrstyrning  
- ✅ Utan automatisk nedladdning  

---

## ✅ Vad fungerar direkt?

- Lokalt AI-system  
- Offline-drift  
- Stöd för lokala modeller  
- Säker start utan internet  
- Ingen plugin-körning  
- Ingen auto-update  
- Ingen bakgrundsövervakning  

---

## ▶ Starta programmet (SAFE MODE)

### Windows
```powershell
venv\Scripts\activate
python launcher.py
```

---

## ⚙ Funktioner som FINNS men är AVSTÄNGDA

Alla funktioner nedan finns installerade i systemet men är **AV** tills användaren själv aktiverar dem:

- Plugins  
- Web Dashboard (lokal)  
- System Monitor  
- License-system  
- Auto-update  
- GPU-detektion  
- Cloud bridge  
- Modell-nedladdare  
- Telemetri  

Styrs via:
```
config/features.json
```
eller via GUI:
```
python launcher_gui.py
```

---

# ⚙️ OFFLINE-AI — ALL FEATURES (OPT-IN)

Detta paket innehåller **HELA systemet med ALLA funktioner**, men fortfarande med:

> ✅ **SAFE DEFAULT – allt är AV som standard**

Användaren väljer själv exakt vad som ska aktiveras.

---

## 🧩 Innehåll i ALL FEATURES-versionen

- Flask Web Dashboard (lokal)  
- Model Manager CLI  
- Plugin-system (sandboxed)  
- Plugin Manager  
- Offline License Generator & Checker  
- System Monitor (psutil)  
- Portable Mode  
- GUI Launcher  
- PyInstaller EXE Builder  
- Inno Setup & NSIS Installer-exempel  
- Plugin Marketplace (lokal)  

---

## 🔧 Default säker konfiguration

```json
{
  "enable_gpu_check": false,
  "enable_auto_update": false,
  "enable_model_downloader": false,
  "enable_telemetry": false,
  "enable_cloud_bridge": false,
  "enable_plugins": false,
  "enable_license_system": false,
  "enable_web_dashboard": false,
  "enable_system_monitor": false
}
```

---

## ▶ Start (ALL FEATURES)

```bash
python launcher_gui.py
```

eller:

```bash
python launcher.py
```

---

## 🌐 Web Dashboard (lokal)

```bash
python -m web.dashboard_app
```

Öppna i webbläsare:
```
http://127.0.0.1:8080
```

---

## 🗂 Model Manager

```bash
python scripts/model_manager.py list
python scripts/model_manager.py info <modell>
python scripts/model_manager.py remove <modell>
```

---

## 🧩 Plugin Manager

Installera plugin:
```bash
python plugins/plugin_manager.py install plugins_market/plugin.zip
```

Kör plugins:
```bash
python plugins/plugin_loader.py
```

---

## 🔐 Licenssystem (offline)

Skapa licens:
```bash
python optional_features/license_generator.py
```

Verifiera licens:
```bash
python optional_features/license_checker.py
```

---

## 🛠 Bygga EXE-filer

```bash
scripts\build_all.bat
```

Installer-exempel finns i:
```
scripts/installer_advanced.iss
scripts/installer_nsis.nsi
```

---

## 🔒 Säkerhetsrekommendationer

- Kör alltid i venv  
- Aktivera endast funktioner du förstår  
- Kontrollera plugins manuellt innan installation  
- Kör helst offline  
- Dela inte din config offentligt  

---

## 📄 Licens & Bidrag

Detta projekt levereras som lokalt/offline-system.  
Lägg till namn i `CONTRIBUTORS.md` om du bidrar.

---

