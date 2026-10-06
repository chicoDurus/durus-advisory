---
title: Launching a Product, Beginning to End
slug: launching-a-product-beginning-to-end
date: 2026-08-04
cover: launch
excerpt: A launch isn't the day you deploy. It starts with a problem worth solving and ends when you know whether it worked. The full sequence, stage by stage, with the checks that matter at each one.
---

Ask most teams when their launch is and they'll give you a deployment date. That's understandable, but it's only one point on a much longer line. Launches fail long before release day, usually because something was skipped early on, and they often fail again afterwards because nobody checks whether the product did what it was meant to do.

Here's the sequence I use, from first idea to measured outcome.

## Stage 1: Define the problem

Before any design or build, write down:

- **The problem** you're solving and who has it
- **The evidence** that it's real: data, user research, support tickets, commercial feedback
- **The outcome** you expect, as a measurable change
- **The constraints:** budget, deadlines, regulatory requirements, technical limits

This is the one-pager stage. Its job is to make sure you're solving a problem worth solving before anyone spends weeks on it.

**Check before moving on:** can you describe success in one sentence that includes a number?

## Stage 2: Discovery and validation

Test the riskiest assumptions as cheaply as you can.

- Talk to users, or to the people who talk to users: support, account managers, sales
- Look at the data you already have: funnels, drop-off points, usage patterns
- Prototype the key flow and put it in front of people
- Check feasibility early with engineering, and compliance requirements with legal

The goal isn't certainty. It's to find out whether you're wrong while it's still cheap to change your mind.

**Check before moving on:** what did you learn that changed the plan? If the answer is "nothing", you probably didn't test the right things.

## Stage 3: Define scope and plan

Now write the PRD and agree what's in the first release. Be ruthless here. The first version should be the smallest thing that delivers the core value and lets you measure the outcome.

At this stage you also need:

- **A dependency map**: other teams, third parties, legal reviews, infrastructure
- **A release plan**: phased rollout, market order, feature flags
- **A measurement plan**: which events to track, which dashboards to build, what baseline you're comparing against

That last point gets skipped constantly. If tracking isn't in scope from the start, it ends up as a ticket after launch, and you lose the first weeks of data.

**Check before moving on:** does every stakeholder agree on what's out of scope?

## Stage 4: Build

Delivery runs in whatever rhythm suits the team. A few things matter more during a launch build than during normal work:

- **Show progress early and often.** Demo partial work to stakeholders so surprises come out in week two, not week ten.
- **Protect the scope.** New ideas go on a "next release" list, not into this one.
- **Track the dependencies weekly.** Third-party integrations and approvals are where launches slip.
- **Build the tracking alongside the feature.** Instrumentation is part of the feature, not an extra.

## Stage 5: Get ready to launch

This stage is about everything around the product.

**Quality**
- Regression testing across devices, browsers and markets
- User acceptance testing with the people who requested it
- Performance and load testing if you expect traffic spikes

**Compliance and risk**
- Legal and compliance sign-off where needed
- Data protection review if personal data is involved
- Rollback plan, written down, with someone named to make the call

**Operational readiness**
- Support briefed, with FAQs and an escalation path
- Internal release notes shared with everyone customer-facing
- Monitoring and alerts in place for the new feature

**Go-to-market**
- Marketing assets and campaign timing agreed
- External messaging reviewed for accuracy, especially any claims
- Account managers or sales briefed if you have B2B clients

I use a launch checklist with an owner for each line. A launch is ready when every line has a tick, not when engineering says the code is done.

## Stage 6: Launch

Some principles for release day itself:

- **Roll out gradually** where you can: one market, one brand or a percentage of users first
- **Use feature flags** so you can switch things off without a redeploy
- **Have the right people available** for the first hours: engineering, support lead, product owner
- **Watch the dashboards**, not just the error logs. Technical health and business health are different things
- **Communicate status** to stakeholders at agreed points, even if the update is "all good"

Avoid launching on a Friday or before a holiday unless there's a strong reason. Small problems are much easier to handle when the team is around.

## Stage 7: Measure and learn

This is where most launches quietly end. The feature ships, the team moves on, and nobody checks whether it worked.

Set a review date before you launch. Two to four weeks is typical, depending on how quickly your metric moves. At that review:

- Compare results against the success measure you set in stage 1
- Look at qualitative signals: support tickets, user feedback, behaviour in session recordings
- Decide what happens next: iterate, scale to more markets, or stop

Write the result into the original PRD. A launch you learn from is worth more than one that simply ships.

## The thread running through it

Each stage protects the next. Weak problem definition makes scope arguments inevitable. Skipping measurement planning makes the final review guesswork. Thin launch readiness turns release day into firefighting.

Products rarely fail at launch because of the code. They fail because one of the earlier stages was rushed, and the cost only appeared later. Give each stage its due, and release day becomes the least dramatic part of the process. That's what you want.
