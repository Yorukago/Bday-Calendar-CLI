# Birthday Calendar

A tiny CLI birthday tracker with wishlists, a month calendar view, and optional terminal reminders.

Data is stored in `~/.local/share/bday/birthdays.json`.

## Requirements

- Python 3.10+
- [Rich](https://github.com/Textualize/rich) (for coloured output)

```bash
pip install -r requirements.txt
```

## Install the `bday` command

Pick one:

```bash
# symlink (adjust paths)
chmod +x /path/to/repo/main.py
ln -sf /path/to/repo/main.py ~/.local/bin/bday

# or alias in fish/bash/zsh
alias bday='python3 /path/to/repo/main.py'
```

Fish users can wrap the same call in a function (for example in `~/.config/fish/config.fish` or a file under `conf.d/`). `$argv` forwards subcommands and flags:

```fish
function bday
    python3 /path/to/repo/main.py $argv
end
```

Ensure the directory containing `bday` is on your `PATH` when you use the symlink install (often `~/.local/bin`). Aliases and Fish functions don’t need that.

## Usage

| Command | What it does |
|--------|----------------|
| `bday add <name> [DD-MM-YYYY]` | Add someone (prompts if date / wishlist missing) |
| `bday add alice 15-06-1999 --wishlist "..." --likes "..."` | Same with flags |
| `bday list` | List everyone |
| `bday search <name>` | Show one person |
| `bday edit <name> [--date …] [--wishlist …] [--likes …]` | Update fields |
| `bday remove <name>` | Remove |
| `bday cal` | Full-screen-ish month calendar |
| `bday check` | Upcoming birthdays (default next **3 days**), or “none” |
| `bday check --days 7` | Longer window |
| `bday remind` | Like `check`, but **prints nothing** if nobody is in range |

`remind` is meant for shell startup hooks: you only see output when someone’s birthday is today or within `--days`.

## Terminal reminders (shell hooks)

Use **`bday remind`** so new terminals quietly show birthdays when relevant.

### Fish (recommended layout)

Copy [`shell/bday-remind.fish`](shell/bday-remind.fish) to:

```
~/.config/fish/conf.d/bday-remind.fish
```

Fish loads everything in `conf.d` automatically, no edits to `config.fish` required.

Optional environment variables:

- `BDAY_REMIND_SKIP=1` — skip reminders for that session (e.g. `env BDAY_REMIND_SKIP=1 fish`)
- `BDAY_REMIND_ARGS` — extra arguments as a space-separated string, e.g. `set -gx BDAY_REMIND_ARGS '-d 7'`

### Bash and Zsh

Add one line to **`~/.bashrc`** or **`~/.zshrc`** (use the real path to this repo):

```bash
[ -r /path/to/bday-calendar/shell/bday-remind.sh ] && . /path/to/bday-calendar/shell/bday-remind.sh
```

Optional:

- `export BDAY_REMIND_SKIP=1` — disable until unset
- `export BDAY_REMIND_ARGS=-d 7` — widen the reminder window

Add your own `LICENSE` file when you publish the repo—this readme stays tiny on purpose.
