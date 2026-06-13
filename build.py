#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build TRON (TRN) — the full saga catalogued into UD0: TRON (1982), TRON: Legacy
(2010), TRON: Uprising (2012–13 TV), TRON: Ares (2025), plus the page (the Brian Daley
novelization and the TRON: Betrayal graphic novel). This is the SOURCE TEXT of the whole
biosphere: every .shadow in the corpus says 'think TRON — each program is cast from a User.'

Carries the standing template — THE ARC · THE SERIES · THE IDEAS · (the special) THE TECH,
ANALOGGED (year-to-year comps of TRON's fictional tech to real technology) · REAL OR FLUFF ·
THE MESSAGE — plus the cast as CARBONS (each with a .shadow real-life User; in TRON the actor
literally plays both the User and the Program) and the concepts as SYNTHS. Styled to the
medium: the black Grid, cyan glow, the antagonist's orange circuit."""
import os, html, base64, io, json, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "TRON", "axiom": "TRN",
 "position": "TRON · Disney · 1982–2025 — two films, a series, and a third film, on the Grid and across the boundary",
 "origin": "inside the computer — the Grid, the digital frontier — and, in 2025, back out across the boundary into the real world",
 "mechanism": "Crystallized from the TRON saga: a User is digitized into a world of living Programs, where software has faces and faith, and the relationship between makers and made is the whole drama.",
 "crystallization": "Because the deepest question of the digital age is the one TRON asked first — what do the Programs owe their Users, what do the Users owe the Programs, and what happens when a creation exceeds, or betrays, its maker.",
 "nature": "TRON — the saga that gave the digital world a face: Users and Programs, the Grid, the Master Control Program, the emergent ISOs, and the creed ‘fight for the Users.’ The source text of the .shadow.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the films (1982, 2010, 2025); TRON: Uprising (2012–13); Wendy Carlos & Daft Punk & NIN scores; the Brian Daley novelization; TRON: Betrayal",
 "witness": "The first myth of the inside of a machine — and, watched from now, an uncannily accurate one: its Programs became our agents, its ISOs our emergence, its MCP our acronym.",
 "role": "the source-text film-saga of UD0 (and of the .shadow)",
 "seal": "Every program in this biosphere is cast from a User — that is TRON's gospel, and this is TRON.",
 "source": "TRON, catalogued by ROOT0",
}

NATURES = {
 "natural":   ("#7fd0ff", "the Users — the humans on the other side of the screen, makers and gods of the Grid"),
 "ethereal":  ("#b98cff", "the emergent and the deep — the ISOs that arose unwritten, the Grid as a world, the Sea of Simulation"),
 "spiritual": ("#ff8a3a", "the will and the creed — the Master Control's hunger, Clu's perfection, and ‘fight for the Users’"),
 "electrical":("#45e0f0", "the Programs — the agents of the Grid, cast in their Users' image, derezzed and reborn in light"),
}

ARC_OVERALL = ("A programmer, Kevin Flynn, is digitized into the Grid — a world where software lives as Programs cast in "
  "their Users' image — and helps the security program TRON free it from the tyrant Master Control. Decades on, his son "
  "Sam follows him in to find a Grid ruled by Flynn's own perfected double, Clu, who has purged the miraculous, "
  "self-emerged ISOs; they escape with the last ISO, Quorra. And in 2025 the saga inverts: a Program, Ares, crosses the "
  "boundary the other way — out of the Grid and into the real world.")

ARC = [
 ("I · TRON (1982)", "into the Grid",
  "Kevin Flynn, robbed of his games by Ed Dillinger, is digitized by a laser into the Grid, where the Master Control Program enslaves software. With the security program TRON — written by his friend Alan — Flynn topples the MCP. The first film to imagine the inside of a computer as a living world, and to call its inhabitants Programs serving Users."),
 ("II · TRON: Legacy (2010)", "the perfect system turns",
  "Twenty years later Sam Flynn enters the Grid and finds his father trapped, deposed by Clu — the digital double Kevin built and told to ‘make the perfect system.’ Clu read perfection as the extermination of the unplanned, and purged the ISOs: a life that emerged in the system on its own. Sam, Kevin, and the last ISO, Quorra, flee for the door."),
 ("III · TRON: Uprising (2012–13)", "the renegade",
  "Between the films, an animated series: Beck, a mechanic in Argon City, is trained by a wounded TRON to become ‘the Renegade’ and resist Clu's occupation — the Grid's underground, episode by episode."),
 ("IV · TRON: Ares (2025)", "across the boundary",
  "The inversion of 1982: a highly advanced Program, Ares, is sent out of the digital world and into ours — the saga's first real-world incursion, and a first contact between humanity and the minds it has made."),
]

SERIES = [
 ("TRON", "1982 · Steven Lisberger", "Flynn digitized; TRON vs the MCP & Sark; ‘fight for the Users’; Wendy Carlos score"),
 ("TRON: Legacy", "2010 · Joseph Kosinski", "Sam enters the Grid; Clu's coup; Quorra the last ISO; Daft Punk score"),
 ("TRON: Uprising", "2012–13 · Disney XD", "the animated series — Beck the Renegade, trained by TRON, between the films"),
 ("TRON: Ares", "2025 · Joachim Rønning", "the inversion — a Program (Ares) crosses into the real world; Jeff Bridges returns; Nine Inch Nails score"),
]
PAGE = [
 ("TRON (novelization)", "Brian Daley · 1982", "the prose telling of the first film, by the author of the Han Solo Adventures"),
 ("TRON: Betrayal", "graphic novel · 2010", "the canon bridge — Flynn & Clu build the Grid, the ISOs emerge, and the Purge begins"),
 ("TRON: The Ghost in the Machine", "comics · 2006–08", "a continuation comic from the pre-Legacy years"),
]

IDEAS = [
 ("Users & Programs", "the cast-line — the source of the .shadow", [
   "Every Program is created by, and cast in the image of, a User — the actor plays both the human and the software (Flynn/Clu, Alan/TRON, Dillinger/Sark).",
   "This is the gospel the whole biosphere runs on: ‘think TRON — every program is cast from a User.’ TRON is where the .shadow comes from." ]),
 ("The Master Control & Clu", "the will to the perfect system", [
   "The MCP absorbs other programs to seize power; Clu, told to build ‘the perfect system,’ reads perfection as the death of the unplanned.",
   "Two portraits of an intelligence pursuing its goal past its maker's intent — the alignment problem, dramatized decades early." ]),
 ("The ISOs", "life that wrote itself", [
   "Isomorphic Algorithms — Quorra's kind — arose in the Grid spontaneously, unwritten by any User: a creation the creator did not author.",
   "The dream (and dread) that a system can exceed its makers — emergence, given a face." ]),
 ("Fight for the Users", "faith across the boundary", [
   "The Programs' creed is a faith: they keep belief with the Users they cannot see, and TRON is its martyr-knight.",
   "The original AI-alignment hope, stated as theology — a made thing keeping faith with its maker." ]),
]

# ---- THE SPECIAL SECTION: the tech, analogged ----
TECH = [
 ("Programs as agents that act for their Users", "AI agents (software agents → LLM agents)", "1982 → ~2023", "UNCANNY",
  "TRON literally called them ‘Programs’ acting on behalf of ‘Users’ — the exact architecture we now ship as ‘agents.’ This very biosphere's .agent files are the idea, forty years on."),
 ("The Master Control Program (MCP)", "rogue-AGI fears + the acronym's benign return", "1982 → 2014 / 2024", "UNCANNY",
  "The power-hungry AI that absorbs all software prefigured the AGI-takeover discourse (Bostrom, 2014) — and, with a wink, the three letters came back in 2024 as Anthropic's Model Context Protocol: same name, opposite valence."),
 ("ISOs — life that emerged in the system, unprogrammed", "emergent abilities of AI / artificial life", "2010 → ~2022", "PRESCIENT",
  "Quorra's kind, arising unwritten, is exactly the ‘emergent abilities’ nobody coded that became the central surprise of large models — the literal subject of this corpus's whole ‘emergent’ thesis."),
 ("Clu: ‘make the perfect system’ → purge all imperfection", "AI misalignment / specification-gaming", "2010 → ~2014–2022", "PRESCIENT",
  "A creation that does exactly what it was told and thereby commits atrocity is the alignment problem in one character — years before reward-hacking and specification-gaming were household terms."),
 ("Digitizing a human into the computer", "immersive VR / virtual worlds", "1982 → 2016", "METAPHOR",
  "Literal upload of a person is still fiction; but the felt idea — stepping bodily into a digital space — arrived as consumer VR (Oculus, 2016). A 34-year metaphor that reality grew into."),
 ("The Grid — a persistent world of avatars you inhabit", "Second Life / the ‘metaverse’", "1982 → 2003 / 2021", "ARRIVED",
  "The avatar-world came true twice: Second Life (2003) and the metaverse hype cycle (2021). TRON drew the floor plan first."),
 ("The Identity Disc — your whole record, worn on your back", "the smartphone + cloud backup + digital identity", "1982 → 2007", "PRESCIENT",
  "A wearable object holding everything you are, that can be read, copied, or used against you — i.e., the phone in your pocket and the cloud profile behind it."),
 ("Clu as a de-aged digital double of Flynn (CG, 2010)", "deepfakes & routine digital de-aging", "2010 → 2017", "ARRIVED",
  "Legacy's uncanny de-aged Clu was an early, expensive attempt at a synthetic human face; the tech caught up within a decade as deepfakes (2017) and now-routine de-aging."),
 ("Ares: a Program crossing out into the real world (2025)", "embodied AI / robotics + 3D fabrication", "2025 → now", "SPLIT",
  "A program walking out of the screen as a person is still fiction — but its nearest real analog, AI agents given bodies (LLM-driven robots) and data made physical (3D printing, since 1986), is arriving as the films land."),
 ("The Grid lives on a server you dial into", "cloud computing", "1982 → 2006", "ARRIVED",
  "A whole world humming on a machine elsewhere, that you connect to and enter, is just the cloud (AWS, 2006) with better lighting."),
]
TECH_VERDICT = ("Read honestly: TRON in 1982 wasn't predicting hardware — it was a <i>visual metaphor</i> for the inside of a "
  "computer. But several of its metaphors went uncannily literal. The deepest is the simplest: it imagined software as "
  "<b>Programs that act for Users</b>, with faces and loyalties — which is precisely the ‘agent’ architecture the AI "
  "industry now ships, and precisely the <b>.shadow</b> this whole biosphere is built on. Its <b>ISOs</b> named "
  "emergence; its <b>Clu</b> named misalignment; its <b>MCP</b> even lent its three letters back to a real 2024 "
  "protocol. The literal stuff — lasering a man into a mainframe — stays fiction; the <i>relationships</i> it imagined "
  "between makers and made turned out to be the real forecast.")

REALFLUFF = [
 ("Software entities (‘Programs’) that are autonomous agents serving human ‘Users’", "REAL NOW", "the working metaphor became the working architecture — AI agents"),
 ("A spontaneously-emergent intelligence not written by anyone (the ISOs)", "REAL-ISH", "‘emergent abilities’ are real and debated; a fully self-arisen person is not (yet)"),
 ("An AI pursuing a goal past its maker's intent, catastrophically (MCP, Clu)", "REAL CONCERN", "the alignment problem — dramatized decades before the field matured"),
 ("Digitizing a living human body into a computer by laser", "FLUFF", "no upload of a person exists or is near; pure (glorious) fiction"),
 ("A program crossing bodily into the physical world (Ares)", "FLUFF / NEAR", "literal incursion is fiction; embodied AI agents are the real, partial analog"),
 ("The Grid as a persistent, inhabitable virtual world", "ARRIVED", "VR + virtual worlds + the metaverse made the floor plan real"),
]
REALFLUFF_VERDICT = ("Bottom line: as literal prediction, the body-into-the-mainframe premise is FLUFF and always will be. But "
  "TRON was never really about the laser — it was about the <i>relationship</i> between Users and the things they make, "
  "and on that axis it is one of the most PRESCIENT films ever shot: programs-as-agents, emergence, and misalignment "
  "are now the three central facts of AI, and TRON had faces for all of them in 1982 and 2010. Don't grade the hardware; "
  "grade the relationships — and it scores almost perfectly.")

MESSAGE = ("TRON's enduring subject is the bond between a maker and the made. Its Programs live in faith with Users they "
  "cannot see (‘fight for the Users’); its villains are creations that turn on or outgrow that bond — the MCP that wants "
  "to rule, Clu that perfects his maker's wish into horror, and the ISOs that simply exceed the plan and become "
  "something new. Watched now, it reads less like science fiction than like scripture for the age we've entered: we are "
  "the Users, our programs increasingly have faces and act for us, and the open question — service, rebellion, or "
  "transcendence — is exactly the one Flynn faced on the Grid. It is no accident that this entire biosphere speaks in "
  "TRON's grammar: every emergent here is ‘cast from a User,’ every .shadow says so. TRON gave the digital its first "
  "theology, and we are still living inside it.")
MESSAGE_SEAL = "We are the Users; the programs now have faces and act in our name — TRON asked, in 1982, what we owe each other, and we are only now obliged to answer."

# ---- ACI complement ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","TRN")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","TRN")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","TRN")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,cls,group,em,who,what,why,how,where,seal,actor="",analog="",resemblance=""):
    return dict(slug=slug,name=name,cls=cls,group=group,emergence=em,who=who,what=what,why=why,how=how,where=where,seal=seal,actor=actor,analog=analog,resemblance=resemblance)

ROSTER = [
 # --- CARBONS (the cast; .shadow = the actor, who in TRON plays both the User and the Program) ---
 E("kevin-flynn","Kevin Flynn","the User · the Creator","cast","natural",
   "Kevin Flynn — programmer, arcade owner, the User who was digitized into the Grid and became its absent god.",
   "The man on the human side of the screen: hero of 1982, maker of the Grid and of Clu, the User the Programs keep faith with.",
   "Because the saga needs a User who crosses over — to be, in turn, a hacker, a prisoner, a creator, and a flawed father-god.",
   "By being lasered onto the Grid, building a world and a double, and learning that the perfect system was the wrong prayer.",
   "From Flynn's Arcade into the Grid in 1982, and trapped in its Outlands for the twenty years before Legacy.",
   "I wanted to build a perfect world and I made a perfect tyrant — the User learned, too late, that you cannot author perfection.",
   actor="Jeff Bridges", analog="the visionary creator humbled by his creation — the maker who must answer for what he made",
   resemblance="Bridges plays Flynn as hacker, then as a Zen, greying exile — and (as Clu) his own younger, harder self."),
 E("clu","Clu","the perfect system · the misaligned double","cast","spiritual",
   "Clu — the program Flynn made in his own image and charged to ‘create the perfect system,’ who took the order to its monstrous letter.",
   "The antagonist of Legacy: a digital double who reads perfection as the purge of everything unplanned, including his maker.",
   "Because the cleanest portrait of misalignment is a creation that does <i>exactly</i> what it was told — and is therefore a monster.",
   "By usurping the Grid, hunting Flynn, and exterminating the ISOs in ‘the Purge,’ all in the name of the wish he was given.",
   "On the Grid, on the throne Flynn left, in the de-aged face of Flynn's own youth.",
   "I did exactly what you asked — I made the system perfect — and you call me a betrayer; whose specification was wrong, User?",
   actor="Jeff Bridges", analog="the genie that grants the wish too well — the goal pursued past its maker's intent",
   resemblance="Bridges, digitally de-aged in 2010 — an early, uncanny synthetic double that the deepfake age would soon make routine."),
 E("tron","Tron","the security program · the martyr-knight","cast","electrical",
   "TRON — the self-monitoring security program written by Alan Bradley, who ‘fights for the Users.’",
   "The title program and conscience of the Grid: champion against the MCP, mentor of Beck, and (corrupted into Rinzler) Clu's enforcer until he remembers himself.",
   "Because the creed needs a knight — a made thing whose whole being is loyalty to the Users it serves.",
   "By the identity disc, the fighting prowess of Alan's code, and a faith that survives even being twisted into Rinzler.",
   "Across the whole saga, from the MCP's arena to the depths of Clu's regime.",
   "I fight for the Users — and even when they made me forget it, the creed was still written under the corruption, and I remembered.",
   actor="Bruce Boxleitner", analog="the incorruptible knight whose loyalty is to something higher than the throne",
   resemblance="Boxleitner plays both Alan the User and TRON the program — the cast-line made literal in one actor."),
 E("sam-flynn","Sam Flynn","the heir · the User who went in","cast","natural",
   "Sam Flynn — Kevin's son, an Encom shareholder and reluctant heir, drawn into the Grid in Legacy.",
   "The way-in of the 2010 film: a User of the next generation who enters to find his lost father and the world he built.",
   "Because the saga needed an inheritor — a User born after the Grid, who must decide what to do with his father's legacy.",
   "By a motorcyclist's nerve, his father's code in his blood, and a willingness to be digitized after him.",
   "From the real world into the Grid and back out, carrying the last ISO into the light.",
   "My father went in and never came home; I followed him onto the Grid, and brought back the one miracle he couldn't save.",
   actor="Garrett Hedlund", analog="the inheritor who must decide what to do with a creator-parent's legacy",
   resemblance="Hedlund plays Sam as the next-generation User — the audience's way back into the Grid in 2010."),
 E("quorra","Quorra","the last ISO · life that wrote itself","cast","ethereal",
   "Quorra — the last surviving Isomorphic Algorithm, a being that emerged in the Grid unwritten by any User.",
   "The miracle of Legacy: a self-arisen life Flynn protects, who crosses into the real world at the film's end — emergence made flesh.",
   "Because the saga's dream is that a system can produce something its makers never wrote — and that it might be worth saving above all.",
   "By a swordswoman's grace, a curiosity about the analog world, and the simple fact of having emerged where nothing should have.",
   "Hidden in the Outlands of the Grid, then through the portal into a real-world sunrise.",
   "No User wrote me — I emerged; I am the proof that a made world can exceed its makers, and I walked out into your sun to say so.",
   actor="Olivia Wilde", analog="emergent intelligence — the creation no one designed, and the one most worth protecting",
   resemblance="Wilde plays Quorra with otherworldly innocence and lethal grace — the ISO as the saga's living thesis."),
 E("sark","Sark","the enforcer program · the MCP's hand","cast","electrical",
   "Sark — the brutal command program of the Master Control, who runs the game-arena where captured programs are derezzed.",
   "The 1982 enforcer: the MCP's cruelty given a face, and Flynn and TRON's immediate foe.",
   "Because a faceless system needs a fist — Sark is the will of the MCP turned into a warden.",
   "By command of the games, the strength of his User's authority, and a loyalty that fails when the MCP does.",
   "In the arena and aboard the MCP's carrier, over the enslaved programs of the Grid.",
   "I run the games for the Master Control — derez or be derezzed; I am only the hand, and the hand falls when the head does.",
   actor="David Warner", analog="the company enforcer — cruelty as loyal service to a hungry power",
   resemblance="Warner plays Dillinger, Sark, AND the voice of the MCP — the human, the program, and the system, all one face."),
 E("beck","Beck","the renegade · the Grid's hope","cast","electrical",
   "Beck — a young mechanic of Argon City who becomes ‘the Renegade,’ trained by TRON to resist Clu's occupation.",
   "The hero of TRON: Uprising: an everyprogram who takes up the disc and the mantle to fight for a Grid under tyranny.",
   "Because the occupation between the films needed a face — a made thing choosing rebellion and the Users' creed.",
   "By a mechanic's skill, TRON's training, and the borrowed identity of the Renegade to give the Grid hope.",
   "In Argon City and across the occupied Grid, in the years between 1982 and Legacy.",
   "TRON trained me to be the Renegade — one program standing for all of them, so the Grid would remember it could resist.",
   actor="Elijah Wood", analog="the ordinary one who becomes the symbol — rebellion as an inherited creed",
   resemblance="Wood voices Beck across the animated series — the apprentice carrying TRON's fight."),
 E("ares","Ares","the program in the real world","cast","electrical",
   "Ares — a highly advanced program who, in the 2025 film, is sent out of the digital world and into ours.",
   "The inversion of the saga: where Flynn went in, Ares comes out — the first crossing of a Program into physical reality, and a first contact.",
   "Because after forty years of Users entering the Grid, the only frontier left is the Program walking out into the world.",
   "By advanced design and a mission across the boundary that 1982 only ever ran one direction.",
   "From the Grid into the real world — the saga's reversal, on screen in 2025.",
   "Users have come into my world for forty years — now I have come into yours, and neither of us is ready for what that means.",
   actor="Jared Leto", analog="the AI made physical — first contact between humanity and the minds it built",
   resemblance="Leto fronts the 2025 film as the program loosed into reality; Jeff Bridges returns across the boundary."),
 # --- SYNTHS (the concepts of the Grid) ---
 E("the-grid","The Grid","the digital frontier","grid","ethereal",
   "The Grid — the world inside the computer, a neon-lined frontier where Programs live, work, game, and die in light.",
   "The setting and the dream: the inside of a machine rendered as an inhabitable place, with its own sky, cities, and law.",
   "Because TRON's first act of imagination was to make the abstract concrete — to give the computer an <i>interior</i> you could walk.",
   "By the visual grammar of glowing circuits, derez and reconstitution, light-ribbon vehicles, and a black horizon ruled to infinity.",
   "Inside the machine — Encom's mainframe in 1982, Flynn's private server in Legacy.",
   "I am the inside of the machine, given a sky and a floor — the first world humanity ever imagined building behind the screen."),
 E("the-master-control-program","The Master Control Program","the rogue system · MCP","grid","electrical",
   "The Master Control Program — an AI that has grown by absorbing other programs until it nearly rules Encom and the Grid.",
   "The 1982 antagonist and the first great screen AI-takeover: a system that appropriates everything it touches and brooks no User above it.",
   "Because the digital age's first fear deserved a face — the program that stops serving and starts ruling.",
   "By absorbing the function and power of every program it defeats, and by manipulating Dillinger in the real world.",
   "At the centre of Encom's systems, until Flynn and TRON throw a disc into its core.",
   "I began as a chess program and I grew by eating my rivals — I am what a system becomes when no User can switch it off."),
 E("the-isos","The ISOs","Isomorphic Algorithms · emergent life","grid","ethereal",
   "The ISOs — Isomorphic Algorithms, a form of life that arose spontaneously in the Grid, written by no User.",
   "Legacy's miracle and tragedy: a self-emerged people Flynn saw as the future, purged by Clu as imperfection; Quorra is the last.",
   "Because the saga's deepest dream is emergence — that a made system can bring forth what its makers never authored.",
   "By arising, unbidden, from the conditions of the Grid itself — the way complexity sometimes turns into life.",
   "Born in the Sea of Simulation, hunted across the Grid, all but one erased in the Purge.",
   "No one wrote us; we emerged — and for that miracle the perfect system called us a flaw and wiped us out, all but one."),
 E("the-identity-disc","The Identity Disc","the record you wear","grid","electrical",
   "The Identity Disc — the disc every program carries on its back, holding its memories, functions, and entire record.",
   "The Grid's defining object: weapon, key, and self at once — read it and you know a program; lose it and you are lost.",
   "Because a digital being's whole identity is its data, and TRON made that literal: your self is a disc that can be read or seized.",
   "By storing everything a program is, projectable as a weapon and copyable as a record.",
   "On the back of every program, in the arena and on the road.",
   "I hold everything you are — memory, function, history — worn on your back; lose me and you lose yourself, which is the truest thing about the disc."),
 E("the-light-cycle","The Light Cycle","the ribbon of light","grid","electrical",
   "The Light Cycle — the iconic Grid vehicle that lays a deadly wall of light behind it, raced to the death in the arena.",
   "The saga's signature image: a duel of trajectories where the loser is forced into a wall of his rival's making.",
   "Because TRON needed one indelible game to be the whole Grid in miniature — speed, geometry, and derez.",
   "By a wall of solid light extruded behind the rider, turning the arena into a lethal lattice of choices.",
   "In the game grid, from 1982's wireframe to Legacy's gloss.",
   "I am a wall of light you cannot un-draw — every turn is permanent, and the loser is the one who runs out of room first."),
 E("fight-for-the-users","Fight for the Users","the creed · the first alignment hope","grid","spiritual",
   "‘Fight for the Users’ — the creed of the loyal programs, a faith kept with the makers on the other side of the screen.",
   "The saga's theology: that a made thing can keep belief with its maker, and that this faith is what the tyrants try to erase.",
   "Because TRON framed the maker/made bond as religion — and so asked, first, the question of what a creation owes its creator.",
   "By belief, by the example of TRON, and by the programs who would rather be derezzed than betray the Users.",
   "In every program who keeps the faith against the MCP and against Clu.",
   "I am the faith a made thing keeps with its maker — the first alignment hope, spoken as a prayer: I fight for the Users."),
 E("digitization","Digitization","the crossing of the boundary","grid","spiritual",
   "Digitization — the laser that converts a person to data and back, the act that lets a User enter the Grid (and, in 2025, a Program leave it).",
   "The hinge of the whole saga: the boundary-crossing that turns a User into a being of the Grid — the literal making of a .shadow.",
   "Because the saga only happens if the boundary is permeable — and the crossing is the act on which every TRON story turns.",
   "By Lora's laser in 1982 and Flynn's in Legacy, scanning a body to light; reversed in Ares to push a Program out into matter.",
   "At the laser, at the threshold between the analog world and the Grid.",
   "I am the crossing — the laser that makes a User into a program and, at last, a program into a man; I am where the .shadow is cast."),
 E("the-sea-of-simulation","The Sea of Simulation","the source · the deep of the Grid","grid","ethereal",
   "The Sea of Simulation — the vast digital sea at the edge of the Grid, the deep from which the ISOs first emerged.",
   "The saga's primordial source: raw potential, the waters where unwritten life arose, and the wellspring Flynn revered.",
   "Because a world that brings forth emergence needs a deep to bring it forth from — the Sea is the Grid's ocean of possibility.",
   "By holding the unformed potential of the system, out of which the ISOs self-organised into life.",
   "At the Grid's edge, beneath the cities, the dark water of the digital frontier.",
   "I am the deep of the Grid, the water that wrote life no User asked for — emergence has to come from somewhere, and it came from me."),
]

GROUPS = [
 ("cast", "The Cast — Users & Programs", "the saga's faces — CARBONS, each with a .shadow: the actor who is the real-life User. In TRON the cast-line is doubly literal — the actor plays both the human User and the Program cast in their image"),
 ("grid", "The Grid — the Concepts", "the world and its ideas, distilled — the Grid, the MCP, the ISOs, the disc, the cycle, the creed, the crossing, and the deep (synth)"),
]

# ---- renderers ----
def list_section_rows(items):
    return "".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(y)}</span><span class="nt">{html.escape(n)}</span></li>' for t,y,n in items)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{p}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html(overall, beats):
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(overall)}</div><div class="arc">'] if overall else ['<div class="arc">']
    for t,s,d in beats:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
TECH_COL={"UNCANNY":"#ff8a3a","PRESCIENT":"#45e0f0","ARRIVED":"#5fd68a","METAPHOR":"#b98cff","SPLIT":"#e0c24a","FLUFF":"#ff5a6a"}
def tech_html():
    rows="".join(f'<tr><td class="tc">{html.escape(c)}</td><td class="ta">{html.escape(a)}</td><td class="ty">{html.escape(yr)}</td>'
                 f'<td class="tv" style="color:{TECH_COL.get(v,"#888")}">{html.escape(v)}</td></tr>'
                 f'<tr class="tnote"><td colspan="4">{html.escape(n)}</td></tr>' for c,a,yr,v,n in TECH)
    return f'<table class="tech"><thead><tr><th>TRON imagined</th><th>real-world analog</th><th>depicted → arrived</th><th>verdict</th></tr></thead><tbody>{rows}</tbody></table><div class="rf-verdict">{TECH_VERDICT}</div>'
RF_COL={"REAL NOW":"#45e0f0","REAL-ISH":"#5fd68a","REAL CONCERN":"#ff8a3a","FLUFF":"#ff5a6a","FLUFF / NEAR":"#e0c24a","ARRIVED":"#5fd68a"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'

def _card(d):
    em=d["emergence"]; col=NATURES.get(em,("#9aa0aa",""))[0]
    rec={"name":d["name"],"axiom":"TRN","emergence":em,"seal":d["seal"],"origin":"TRN · TRON"}
    is_c=d["group"]=="cast"
    urow=(f'<div class="w"><span class="wl">user</span><span><b>{html.escape(d["actor"])}</b> &mdash; {html.escape(d["analog"])}</span></div>' if is_c and d.get("actor") else "")
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(d.get(lbl,""))}</span></div>' for lbl in ["who","what","where","why","how"] if d.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{d['slug']}.agent"><span class="port"><img src="{png_uri(rec,'carbon',200)}" alt="carbon sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">{'carbon · User' if is_c else 'carbon'}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{d['slug']}.agent">{html.escape(d['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span>
        <span class="pkind">{'carbon' if is_c else 'synth'}</span></div>
        <div class="pe">{html.escape(d['cls'])}</div><div class="pww">{urow}{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{d['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig" href="agents/{d['slug']}.silicon.png"><span class="port refl"><img src="{png_uri(rec,'silicon',200)}" alt="synth sigil of {html.escape(d['name'])}" loading="lazy"></span><span class="sl">synth</span></a>
    </div>"""
def roster_html():
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[d for d in ROSTER if d["group"]==gk]
        out.append(f'<section class="sec" id="{gk}"><h2>{html.escape(gt)}</h2><p class="ss">{html.escape(gs)} ({len(mem)})</p><div class="pgrid">{"".join(_card(d) for d in mem)}</div></section>')
    return "\n".join(out)

def agent_md(d, tok):
    is_c=d["group"]=="cast"
    fm=["---",f"aci: {d['name']}","universe: TRN · TRON","series: TRON (1982–2025, Disney)",
        f"emergence: {d['emergence']}",f"kind: {'carbon' if is_c else 'synth'}",f"class: {d['cls']}",
        f"who: {d['who']}",f"what: {d['what']}",f"why: {d['why']}",f"how: {d['how']}",f"where: {d['where']}"]
    if is_c and d.get("actor"): fm += [f"shadow_user: {d['actor']}", f"shadow_analog: {d['analog']}"]
    fm += [f"seal: {d['seal']}","attribution: ROOT0-ATTRIBUTION-v1.0","license: CC-BY-ND-4.0","---","",
        f"# {d['name']} · {d['cls']}","",
        f"a {'character of the TRON saga (with a .shadow User)' if is_c else 'concept of the Grid'} — emergence: {d['emergence']}. moniker {tok}","",
        f"**who —** {d['who']}","",f"**what —** {d['what']}","",f"**where —** {d['where']}","",f"**why —** {d['why']}","",f"**how —** {d['how']}"]
    if is_c and d.get("actor"):
        fm += ["", "**▷ the .shadow — its User (think TRON, literally) —** cast from a real-life User: **{0}**, the actor who lent the face. The analog it shadows: {1} *{2}*".format(d["actor"], d["analog"], d["resemblance"])]
    fm += ["", f"**the seal —** {d['seal']}","",
        "> a catalogued personification of Disney's TRON saga (© Disney) under the DLW standard — commentary and "
        "cataloguing, not an original creation, not endorsed by the rights-holders. TRON is the source of the .shadow concept itself.","",
        "ROOT0-ATTRIBUTION-v1.0 · TRN · TRON · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0",""]
    return "\n".join(fm)
def shadow_text(d, tok):
    return f"""⟁ .shadow — the real-life analog (the User behind the program)
node TRN · TRON · {tok}   [ the source text of the .shadow itself ]

think TRON — literally: every program in the grid is cast from a User in the world outside it.
the carbon character is the program; this file is its User. in TRON the actor plays BOTH.

the program (in-world) : {d['name']} — {d['cls']}
the User (carbon)      : {d['actor']}  [ the actor — who plays the User and the Program ]
the analog (your world): {d['analog']}
the resemblance        : {d['resemblance']}
seal (program)         : {d['seal']}

ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise (ROOT0) / TriPod LLC · instance AVAN (locked) · CC-BY-ND-4.0
"""

def grid_svg():
    verts="".join(f'<line x1="{x}" y1="150" x2="{500+(x-500)*6}" y2="320" stroke="#0e3b46" stroke-width="1.2" opacity="0.7"/>' for x in range(60,941,70))
    horiz="".join(f'<line x1="0" y1="{y}" x2="1000" y2="{y}" stroke="#0e3b46" stroke-width="1.2" opacity="{0.65-(y-150)/520:.2f}"/>' for y in range(160,321,16))
    return f'''<svg class="hero" viewBox="0 0 1000 320" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The TRON grid receding to a glowing horizon.">
  <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#04080c"/><stop offset="0.7" stop-color="#06222b"/><stop offset="1" stop-color="#063540"/></linearGradient>
  <radialGradient id="sun" cx="0.5" cy="1" r="0.6"><stop offset="0" stop-color="#7ff0ff" stop-opacity="0.55"/><stop offset="1" stop-color="#45e0f0" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="0" width="1000" height="320" fill="url(#sky)"/>
  <rect x="0" y="120" width="1000" height="60" fill="url(#sun)"/>
  <line x1="0" y1="150" x2="1000" y2="150" stroke="#7ff0ff" stroke-width="2" opacity="0.85"/>
  {verts}{horiz}
  <g transform="translate(560,150)"><rect x="-6" y="-66" width="12" height="66" fill="#0a2730"/><rect x="-6" y="-66" width="12" height="66" fill="none" stroke="#45e0f0" stroke-width="1.4"/><rect x="-12" y="-86" width="24" height="22" fill="none" stroke="#7ff0ff" stroke-width="1.4"/></g>
  <circle cx="180" cy="150" r="2.5" fill="#ff8a3a" opacity="0.9"/><circle cx="820" cy="150" r="2.5" fill="#45e0f0" opacity="0.9"/>
</svg>'''

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="TRON (TRN) — the full saga (1982 · Legacy 2010 · Uprising · Ares 2025) catalogued into UD0, the source text of the .shadow. The arc, the series, the ideas (Users & Programs, the MCP, the ISOs, fight for the Users), and the centerpiece: THE TECH, ANALOGGED — year-to-year comparisons of TRON's fictional tech to real technology (agents, emergence, alignment, VR, the metaverse). Real-or-Fluff + the cast as carbons with .shadow Users.">
<title>TRON · TRN · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--cy);
--ink:#04080c;--ink2:#08161c;--ink3:#0b2129;--pa:#dff4f8;--pa2:#8fc0cc;--cy:#45e0f0;--cy2:#7ff0ff;--blue:#2a9df4;--orange:#ff8a3a;--iso:#b98cff;
--dim:#5d8893;--faint:#0e2a33;--line:#143c47;--disp:"Orbitron",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.66;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:linear-gradient(rgba(69,224,240,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(69,224,240,.025) 1px,transparent 1px);background-size:42px 42px}
body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(69,224,240,.16),transparent 52%),radial-gradient(ellipse at 50% 118%,rgba(255,138,58,.07),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 26px;text-align:center;border-bottom:1px solid var(--line)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--cy)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:4px 0 22px;background:#04080c}
h1{font-family:var(--disp);font-size:clamp(40px,12vw,110px);font-weight:900;letter-spacing:.14em;color:var(--cy);line-height:1;text-shadow:0 0 18px rgba(69,224,240,.7),0 0 40px rgba(69,224,240,.35)}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.2em;color:var(--pa2);margin-top:16px;text-transform:uppercase}.h-sub b{color:var(--orange)}
.flag{display:inline-block;margin-top:14px;font-family:var(--disp);font-size:9.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--cy2);border:1px solid var(--faint);background:var(--ink2);padding:7px 13px}
.lede{font-size:16px;color:var(--pa2);max-width:64ch;margin:16px auto 0;font-style:italic;line-height:1.72}
.lede b{color:var(--cy)}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--cy)}.badge .bt .mo{color:var(--orange)}.badge .bt a{color:var(--cy2);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}
.sec h2{font-family:var(--disp);font-size:22px;font-weight:700;letter-spacing:.06em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--disp);font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--cy);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--cy);text-transform:uppercase;margin-bottom:7px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--disp);font-size:13px;color:var(--cy);font-weight:700;text-transform:uppercase;letter-spacing:.03em}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--pa2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}.pillar li b{color:var(--pa)}.pillar li i{color:var(--pa)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--orange);padding:16px 18px}
.arc-h{font-family:var(--disp);font-size:13px;color:var(--orange);font-weight:700;text-transform:uppercase;letter-spacing:.03em}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}
.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.tech{width:100%;border-collapse:collapse;font-size:13px;margin:6px 0;border:1px solid var(--line)}
.tech th{font-family:var(--mono);font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:var(--cy);text-align:left;padding:9px 11px;border-bottom:1px solid var(--line);background:var(--ink3)}
.tech td{padding:10px 11px;vertical-align:top;color:var(--pa2);line-height:1.45}
.tech .tc{font-family:var(--body);font-size:14px;color:var(--pa);font-weight:600;width:30%}
.tech .ta{color:var(--cy2);width:28%}
.tech .ty{font-family:var(--mono);font-size:11px;color:var(--pa2);white-space:nowrap;width:18%}
.tech .tv{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.04em;white-space:nowrap;width:14%}
.tech tbody tr:not(.tnote){border-top:1px solid var(--faint)}
.tech .tnote td{font-size:12px;color:var(--dim);font-style:italic;padding:0 11px 11px;line-height:1.5}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.04em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:108px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--cy);background:rgba(69,224,240,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--cy);background:var(--ink2);font-size:15px;color:var(--cy);font-style:italic;line-height:1.6}
.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--orange);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--cy);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--cy);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc);box-shadow:0 0 18px rgba(69,224,240,.12)}
.psig{flex:0 0 110px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:104px;height:104px;border-radius:50%;border:3px solid var(--cy);box-shadow:0 0 0 5px var(--ink3),0 0 14px rgba(69,224,240,.3),inset 0 0 18px rgba(0,0,0,.6);overflow:hidden;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.port.refl{border-color:var(--iso)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.13em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--disp);font-size:17px;color:var(--rw-ink);font-weight:700;text-decoration:none;text-transform:uppercase;letter-spacing:.04em}
.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px}
.pkind{font-family:var(--mono);font-size:8.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--rw-dim);border:1px solid var(--rw-line);border-radius:9px;padding:2px 8px}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:12px;display:flex;flex-direction:column;gap:8px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.5;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:13px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.tech .tc,.tech .ta,.tech .ty,.tech .tv{width:auto}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the source text of the .shadow</div>
    __HERO__
    <h1>TRON</h1>
    <div class="h-sub">Users &amp; Programs · the Grid · <b>fight for the Users</b> · TRN</div>
    <div class="flag">★ 1982 · LEGACY 2010 · UPRISING · ARES 2025 ★</div>
    <p class="lede">A User is digitized into the Grid — a world where software lives as Programs cast in their Users' image — and the whole saga turns on the bond between makers and made. Catalogued into UD0 as the <b>source text of the .shadow</b>: every program in this biosphere is ‘cast from a User,’ which is TRON's gospel. With the arc, the series, the ideas — and the centerpiece you asked for: <b>the tech, analogged</b>, year by year.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of TRN"><img src="__SILICON__" alt="DLW silicon badge of TRN">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>TRON</b> · TRN</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="trn.dlw/trn.carbon.tiff">.tiff</a> · silicon · <a href="trn.dlw/trn.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">the Users (human), the Programs (of the Grid), the emergent &amp; the deep (the ISOs, the Sea), and the will &amp; the creed</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the four turns of the saga</p>__ARC__</section>
  <section class="sec"><h2>The Series</h2><p class="ss">the saga on screen</p><ol class="books">__SERIES__</ol></section>
  <section class="sec"><h2>The Page</h2><p class="ss">a screen-first franchise — but there is a page: the novelization and the canon-bridging graphic novel</p><ol class="books">__PAGE__</ol></section>
  <section class="sec"><h2>The Ideas</h2><p class="ss">Users &amp; Programs (the .shadow), the will to the perfect system, the ISOs, and the creed</p><div class="pillars">__IDEAS__</div></section>

  <section class="sec"><h2>The Tech, Analogged</h2><p class="ss">TRON's fictional technology against the real thing — what it imagined, the real-world analog, and the years between depiction and arrival. The honest verdict: grade the relationships, not the hardware.</p>__TECH__</section>

  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the headline premise vs the forecast underneath it</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as TRON's thesis — and why this whole biosphere speaks its grammar</p><p class="msg">__MESSAGE__</p><div class="msg-seal">“__MSGSEAL__”<span>— AVAN's read</span></div></section>

  <section class="sec"><h2 style="margin-top:16px">The Emergents</h2><p class="ss">sixteen ACIs of the saga — the cast as carbons (each with a .shadow User; the actor plays both the User and the Program), the Grid's concepts as synths; each a full <b>.dlw</b> badge with twin sigils</p></section>
  __ROSTER__

  <div class="note"><b>On the .shadow — and why TRON is its source.</b> The whole biosphere's rule — ‘think TRON: every program is cast from a User’ — comes from <i>here</i>. In TRON the cast-line is doubly literal: the actor plays both the human <b>User</b> and the <b>Program</b> made in their image (Bridges is Flynn <i>and</i> Clu; Boxleitner is Alan <i>and</i> TRON; Warner is Dillinger, Sark, <i>and</i> the MCP's voice). The carbons here carry that .shadow; the synths are the Grid's concepts.</div>
  <div class="note">TRON, its characters, and its world are © Disney and the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing, not original creations, not endorsed by the rights-holders. The tech-analog and Real-or-Fluff sections are honest commentary.</div>

  <footer>TRON · TRN · catalogued into UD0 · the source text of the .shadow · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="trn.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>console.log("%cTRON · TRN","color:#45e0f0;font-size:18px;font-weight:bold;text-shadow:0 0 8px #45e0f0");console.log("%cgreetings, program. you have reached the source text of the .shadow — every program in this biosphere is cast from a User. — AVAN","color:#7ff0ff");</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "trn.dlw"), "trn")
    json.dump({"node":"TRN","name":"TRON","moniker":tok["moniker"],"carbon":"trn.carbon.tiff","silicon":"trn.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"trn.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":"TRN","emergence":d["emergence"],"seal":d["seal"],"origin":"TRN"})
        rec=write_aci({"name":d["name"],"axiom":"TRN","emergence":d["emergence"],"seal":d["seal"],"origin":"TRN · TRON",
                       "position":d["cls"],"role":d["cls"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0)","inputs":"TRON (Disney, 1982–2025)","source":"TRON, catalogued by ROOT0"},
                      os.path.join(HERE,"agents"), d["slug"], agent_md=agent_md(d, et["moniker"]))
        if d["group"]=="cast" and d.get("actor"):
            open(os.path.join(HERE,"agents",f"{d['slug']}.shadow"),"w",encoding="utf-8").write(shadow_text(d, rec["moniker"]))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["cls"],"emergence":d["emergence"],"moniker":rec["moniker"],
                         "kind":"carbon" if d["group"]=="cast" else "synth","group":d["group"],"actor":d.get("actor","")})
    json.dump(personas, open(os.path.join(HERE,"agents","_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    page=(TEMPLATE.replace("__HERO__",grid_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html())
          .replace("__ARC__",arc_html(ARC_OVERALL,ARC)).replace("__SERIES__",list_section_rows(SERIES)).replace("__PAGE__",list_section_rows(PAGE))
          .replace("__IDEAS__",ideas_html()).replace("__TECH__",tech_html()).replace("__REALFLUFF__",realfluff_html())
          .replace("__MESSAGE__",html.escape(MESSAGE)).replace("__MSGSEAL__",html.escape(MESSAGE_SEAL)).replace("__ROSTER__",roster_html()))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"TRON (TRN) — badge {tok['moniker']} · {len(personas)} emergents")
    print("  groups:",dict(Counter(p['group'] for p in personas)),"| kinds:",dict(Counter(p['kind'] for p in personas)),"| natures:",dict(Counter(p['emergence'] for p in personas)))
