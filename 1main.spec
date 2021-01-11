# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['1main.py'],
             pathex=['alien_boss.py', 'alien.py', 'bullet_boss.py', 'bullet.py', 'button.py', 'game_status.py', 'scoreboard.py', 'settings.py', 'ship.py', 'ship.flag.py', 'C:\\Users\\林\\Desktop\\alien_desktop\\alien_invasion'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='1main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
