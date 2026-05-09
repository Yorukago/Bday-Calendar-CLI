#!/usr/bin/env python3
import argparse
import sys

import database
import visuals


def cmd_add(args):
    name = args.name
    date = args.date or input("Date (DD-MM-YYYY): ")
    wishlist = args.wishlist or input(f"What does {name} want? ")
    likes = args.likes or input(f"What does {name} like? ")
    ok, msg = database.add_person(name, date, wishlist, likes)
    (visuals.ok if ok else visuals.err)(msg)


def cmd_remove(args):
    ok, msg = database.remove_person(args.name)
    (visuals.ok if ok else visuals.err)(msg)


def cmd_edit(args):
    ok, msg = database.edit_person(args.name, args.date, args.wishlist, args.likes)
    (visuals.ok if ok else visuals.err)(msg)


def cmd_search(args):
    result = database.search_person(args.name)
    if result:
        visuals.print_person(result)
    else:
        visuals.err(f"Couldn't find '{args.name}'.")


def cmd_list(_args):
    data = database.load_data()
    visuals.print_list(data)


def cmd_cal(_args):
    data = database.load_data()
    visuals.show_calendar(data)


def cmd_check(args):
    days = getattr(args, "days", 3)
    upcoming = database.get_upcoming(days_ahead=days)
    if upcoming:
        visuals.print_upcoming(upcoming)
    elif not getattr(args, "quiet", False):
        visuals.ok(f"No birthdays in the next {days} days.")


def cmd_remind(args):
    """For shell startup: print only when someone's birthday is in range; otherwise silent."""
    days = getattr(args, "days", 3)
    upcoming = database.get_upcoming(days_ahead=days)
    if upcoming:
        visuals.print_shell_reminder_banner()
        visuals.print_upcoming(upcoming)


def build_parser():
    parser = argparse.ArgumentParser(
        prog="bday",
        description="✨ Yoru's Birthday Tracker",
    )
    sub = parser.add_subparsers(dest="command", metavar="command")
    sub.required = True

    # add
    p_add = sub.add_parser("add", help="add a person")
    p_add.add_argument("name", help="person's name")
    p_add.add_argument("date", nargs="?", help="birthday DD-MM-YYYY")
    p_add.add_argument("--wishlist", "-w", help="their wishlist")
    p_add.add_argument("--likes", "-l", help="things they like")
    p_add.set_defaults(func=cmd_add)

    # remove
    p_rm = sub.add_parser("remove", aliases=["rm", "delete"], help="remove a person")
    p_rm.add_argument("name")
    p_rm.set_defaults(func=cmd_remove)

    # edit
    p_edit = sub.add_parser("edit", help="edit a person's info")
    p_edit.add_argument("name")
    p_edit.add_argument("--date", "-d")
    p_edit.add_argument("--wishlist", "-w")
    p_edit.add_argument("--likes", "-l")
    p_edit.set_defaults(func=cmd_edit)

    # search
    p_search = sub.add_parser("search", help="look someone up")
    p_search.add_argument("name")
    p_search.set_defaults(func=cmd_search)

    # list
    p_list = sub.add_parser("list", aliases=["ls"], help="list everyone")
    p_list.set_defaults(func=cmd_list)

    # cal
    p_cal = sub.add_parser("cal", help="show calendar view")
    p_cal.set_defaults(func=cmd_cal)

    # check
    p_check = sub.add_parser("check", help="check upcoming birthdays")
    p_check.add_argument("--days", "-d", type=int, default=3, help="how many days ahead (default: 3)")
    p_check.add_argument("--quiet", "-q", action="store_true", help="no output if nothing coming up")
    p_check.set_defaults(func=cmd_check)

    # remind (quiet check — handy in ~/.bashrc or fish greeting)
    p_remind = sub.add_parser(
        "remind",
        help="print upcoming birthdays if any (silent if none); for terminal startup hooks",
    )
    p_remind.add_argument("--days", "-d", type=int, default=3, help="how many days ahead (default: 3)")
    p_remind.set_defaults(func=cmd_remind)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
