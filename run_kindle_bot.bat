
set filename=C:\Users\uncle\AppData\Local\Amazon\Kindle\Cache\KindleSyncMetadataCache.xml
set appPath=C:\Users\uncle\AppData\Local\Amazon\Kindle\application\Kindle.exe


for %%i in (%filename%) do set "update_date=%%~ti"

start %appPath%

:chech_xml
for %%i in (%filename%) do set "new_update_date=%%~ti"
if "%update_date%" == "%new_update_date%" (
    goto :chech_xml
  ) else (
    :check_start_app
    tasklist | find "Kindle.exe" > NUL
    if %ERRORLEVEL% == 0 (
      python F:\git\kindle_reading_volume\tweet.py
      taskkill /F /T /IM "Kindle.exe"
      pause
    ) else (
      goto :check_start_app
    )
)


