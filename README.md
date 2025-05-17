# Lockr

![Logo](Lockr.png)

A simple password generator that lives in your terminal.
## Installation

1. Clone the repository.

    ```
    gh repo clone Gal-ahad/Lockr
    ```
2. Download pyinstaller.
    ```
    pip install pyinstaller
    ```
3. The convert the script to an executable.
    ```
    pyinstaller --onefile lockr.py
    ```

#### Alternatively

Download the latest [release](https://github.com/Gal-ahad/Lockr/releases). The executable should be placed in a folder that's included in `PATH` (see [this guide](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) on how to do that)
## Documentation

```
usage: lockr [-h] [--remove-special] length

Generate a secure password

positional arguments:
  length            How long should your password be, from 12 to 20

options:
  -h, --help        show this help message and exit
  --remove-special  Remove special characters (off by default)
```

## Roadmap

- [ ]  Exclude certain symbols
- [ ]  Custom min/max characters
- [ ]  Generate multiple passwords
- [ ]  Save password(s) to file
- [ ]  Settings
- [ ]  Generation history
- [ ]  GUI version

## Support

For support, please head over to my [profile's readme](https://github.com/Gal-ahad/Gal-ahad?tab=readme-ov-file#-find-me-elsewhere).
Or you can [buy me a coffee](https://ko-fi.com/ga1_ahad)

## License

[GNU General Public License v3.0](https://github.com/Gal-ahad/Lockr/blob/main/LICENSE)
