# Birthday reminder for Bash AND Zsh (silent if nothing upcoming).
# Install: add ONE line to ~/.bashrc or ~/.zshrc:
#   [ -r /path/to/this/repo/shell/bday-remind.sh ] && . /path/to/this/repo/shell/bday-remind.sh
# Requires `bday` on PATH (see README).
# Skip once: BDAY_REMIND_SKIP=1 bash   (same idea for zsh)
# Extra args passed to remind: export BDAY_REMIND_ARGS="-d 7"

# Bash & Zsh: interactive only
case $- in
    *i*) ;;
    *) return ;;
esac

if [ -n "${BDAY_REMIND_SKIP:+x}" ]; then
    return
fi

if command -v bday >/dev/null 2>&1; then
    # shellcheck disable=SC2086
    bday remind ${BDAY_REMIND_ARGS:-} 2>/dev/null
fi
