# Birthday reminder on Fish startup (silent if nothing upcoming).
# Install: copy this file to ~/.config/fish/conf.d/bday-remind.fish
# Requires `bday` on PATH (see README).
# Skip for one session:  BDAY_REMIND_SKIP=1 fish
# Skip forever: remove this file from conf.d

status is-interactive; or return

set -q BDAY_REMIND_SKIP; and return

if command -vq bday
    if set -q BDAY_REMIND_ARGS; and test -n "$BDAY_REMIND_ARGS"
        command bday remind (string split ' ' -- $BDAY_REMIND_ARGS) 2>/dev/null
    else
        command bday remind 2>/dev/null
    end
end
