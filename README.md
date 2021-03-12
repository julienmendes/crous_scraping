# WEB SCRAPPING CROUS DE FRANCE

**EDIT non fonctionnel**

Cet outil a pour objectif d'identifier les disponibilités des chambres proposées par le Crous.
Très utile pour Paris notamment où il faut être très réactif pour obtenir une chambre.
Lorsque le script tourne il interroge de façon régulière l'URL renseigné et lorsqu'un logement est disponible un mail automatique est envoyé avec les départements de ces logements.

**Comment trouver l'URL:**
il suffit de se rendre sur le lien suivant (https://trouverunlogement.lescrous.fr/tools/flow/16/search?bounds=-10.5469_55.0784_14.9854_36.1379&page=1&price=60000) et à l'aide des outils de zoom d'ajuster sur la carte la zone de recherche souhaitée.
Enfin copiez l'URL de cette page.

**Paramètres**
URL: lien de la page de recherche
MAIL: addresse mail ou l'on souhaite recevoir les informations mais aussi celle qui va envoyer les mails
MAIL_mdp: mot de passe de la boite mail

**Important**
Il faut parametrer une plus grande liberté a son compte mail pour que l'API smtplib puisse exploiter la boite mail.

**Limites et améliorations:**
le script est très sensible aux modifications du code sources du site du crous. Il faut donc le modifier en conséquence.
Dans le cas où de nombreux logements sont disponibles il est possible de recevoir plusieurs mails à cause de l'ordre des codes postaux qui ne sont pas dans le même ordre. Piste d'amélioration, trier les codes postaux par ordre croissant.

Dernière utilisation: Mars 2020