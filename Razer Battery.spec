# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['razer_battery_tray.py'],
    pathex=[],
    binaries=[],
    datas=[('resources', 'resources')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(  # noqa: F821
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="Razer Battery",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['resources/AppIcon.icns'],
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Razer Battery',
)
app = BUNDLE(
    coll,
    name='Razer Battery.app',
    icon='resources/AppIcon.icns',
    bundle_identifier=None,
)
