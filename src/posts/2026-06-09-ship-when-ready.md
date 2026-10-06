---
title: Ship When It's Ready, Not When the Calendar Says So
slug: ship-when-its-ready
date: 2026-06-09
cover: calendar
excerpt: Fixed release trains look disciplined on a slide. In practice they hold back finished work and push unfinished work out the door. Why we prefer releasing when work is ready, and what it takes to do that safely.
---

Many product organisations run on a fixed release calendar. Every second Tuesday, or the first Monday of the month, whatever has made it in goes out.

It looks orderly. Leadership knows when to expect changes, marketing can plan around it, and nobody has to make a judgement call about timing.

We think it's usually the wrong default, and that the cost is mostly invisible to the people who set it up.

## What a fixed calendar actually does

A release date is a deadline that ignores the state of the work.

When a feature is finished on Wednesday and the next release is in twelve days, it sits on a shelf. Nobody gets value from it, nobody learns whether it works, and the team has already moved on by the time it reaches customers.

When a feature is nearly finished on release day, the pressure runs the other way. Testing gets compressed, a known issue gets labelled "minor", and something goes out that shouldn't have. Then the next cycle starts with a fix.

Software delivery is full of surprises: a third-party API that changes its behaviour, a security review that takes longer than planned, a production issue that pulls two engineers away for three days. A calendar fixed in advance can't absorb any of that. It just moves the risk somewhere else.

## Releasing when the work is ready

Our preference is ad hoc releases. A change goes out when it's built, tested and safe to release, whether that's Tuesday afternoon or three times in one week.

This has some practical advantages for the business:

- value reaches customers as soon as it exists
- each release is smaller, so it's easier to test and easier to roll back
- problems show up one change at a time, instead of buried in a bundle of twenty
- nobody rushes work to make a date that was set months ago

It also changes the conversation with leadership. Instead of "what's in the next release?", the question becomes "what's done, and what did it change?" That's a much better question.

## What has to be true first

Releasing ad hoc still takes discipline. A few things need to be in place first.

You need automated testing good enough that a release doesn't require a week of manual regression. You need a deployment process that's boring: one click or one merge, the same every time. You need a way to switch features off without a redeploy, so a problem in production is a toggle away from contained. And you need monitoring that tells you within minutes if something has gone wrong.

Most of this is ordinary engineering hygiene. If your team can't release safely on short notice today, that's worth knowing regardless of which release model you choose, because you'll need to on the day something breaks.

## Where fixed dates still make sense

Some changes do need a date. A regulatory requirement with a legal deadline. A launch tied to a marketing campaign, an event or a partner announcement. A change that needs customers or support teams to be warned in advance.

For those, set a date for the business event and keep the engineering release flexible underneath it. Ship the code early behind a feature switch, test it in production with internal users, and turn it on when the date arrives. The date becomes a business decision, not an engineering constraint.

## What leadership should ask for instead

If you want predictability, ask for it in the right place. Not "when is the next release?" but:

- what's finished since last week, and what's it doing for customers?
- what's at risk, and what are the options?
- what's coming in the next few weeks, roughly?

A team that can answer those clearly gives you more control than any release calendar, without the hidden cost of work waiting on a shelf or going out half-tested.
