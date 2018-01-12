
# Copyright: 2018 rfglenn
# License: GNU AGPL, version 3 or later; http://www.gnu.org/copyleft/agpl.html
#
# update fields on answer: updates card fields on answer according to their interval length
# GitHub: https://github.com/rfglenn/


from anki.hooks import wrap
from anki.sched import Scheduler


#updateSet = [("Note Model", "Card Model"):("Field", [("string", interval),...]),...]
#edit this stuff right here
updateSet = {
    ("Heisig", "Key->Kanji"): ("Keyword Familiarity", [("new", 0), ("young",30), ("mature",90)]),
    ("Heisig", "Kanji->Key"): ("Kanji Familiarity", [("new", 0), ("young",30), ("mature",90)])
    }


def matureCheck(self, card, ease):
    note = card.note()
    
    modelname = note.model()['name']
    cardtype = card.template()['name']

    update = updateSet.get((modelname, cardtype))
    
    if update is None:
        return True
        
    (maturityField, cutoff) = update
    for (descriptor, age) in cutoff:
        if (card.ivl >= age):
            note[maturityField] = descriptor
                
    note.flush()
    return True

Scheduler.answerCard = wrap(Scheduler.answerCard, matureCheck)



