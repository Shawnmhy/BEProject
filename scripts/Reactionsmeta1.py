from Recon.models import Reactionsmeta, StoichiometryMetabolite1


def convert_reactions_meta():

    for id in Reactionsmeta.objects.all():
        for i in range(1,61):
            current_metabolite = getattr(Reactionsmeta, 'metabolite'+'i', None)
            if current_metabolite is not None:
                StoichiometryMetabolite1.objects.create(meatabolite=current_metabolite, id=id)

