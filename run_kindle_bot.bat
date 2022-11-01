
set filename=C:\Users\uncle\AppData\Local\Amazon\Kindle\Cache\KindleSyncMetadataCache.xml
set appPath=C:\Users\uncle\AppData\Local\Amazon\Kindle\application\Kindle.exe


for %%i in (%filename%) do set "update_date=%%~ti"

start %appPath%

timeout /t 180 /nobreak
taskkill /F /T /IM "Kindle.exe"
timeout /t 10 /nobreak

:chech_xml
for %%i in (%filename%) do set "new_update_date=%%~ti"
if "%update_date%" == "%new_update_date%" (
    goto :chech_xml
  ) else (
    :check_start_app
    tasklist | find "Kindle.exe" > NUL
    if %ERRORLEVEL% == 1 (
      python F:\git\kindle_reading_volume\tweet.py
      pause
    ) else (
      goto :check_start_app
    )
)


