# NoTracker

Bot Discord qui détecte et retire automatiquement les paramètres de tracking des liens partagés dans un serveur.

**Exemple :**

Chris envoie :
> `Regarde cette vidéo https://youtu.be/5uQgPimX7vU?si=Flwg59P8om9voa8b`

Le bot supprime le message et le reposte ainsi :
> **Chris** : Regarde cette vidéo https://youtu.be/5uQgPimX7vU
> *🔗 Liens nettoyés des trackers*

## Trackers supprimés

- `?si` — YouTube
- `?utm_*` — Google Analytics (présent sur la plupart des sites)
- `?fbclid` — Facebook
- `?gclid` — Google Ads
- `?msclkid` — Microsoft Ads
- `?ref`, `?referrer` — générique
- `?mc_cid`, `?mc_eid` — Mailchimp

## Installation

**1. Cloner le repo**
```bash
git clone <url-du-repo>
cd NoTracker
```

**2. Installer les dépendances**
```bash
pip install -r requirements.txt
```

**3. Configurer le token**

Copier `.env.example` en `.env` et y mettre ton token :
```bash
cp .env.example .env
```
```
DISCORD_TOKEN=ton_token_ici
```

**4. Lancer le bot**
```bash
python bot.py
```

## Configuration Discord

### Developer Portal

1. Aller sur [discord.com/developers/applications](https://discord.com/developers/applications)
2. Créer une nouvelle application → **Bot**
3. Copier le token et le mettre dans `.env`
4. Dans **Bot → Privileged Gateway Intents**, activer :
   - ✅ **Message Content Intent**

### Inviter le bot sur ton serveur

Dans **OAuth2 → URL Generator** :

- **Scopes :** `bot`
- **Permissions :**
  - ✅ Read Messages / View Channels
  - ✅ Send Messages
  - ✅ Read Message History
  - ✅ Manage Messages

Copier l'URL générée et l'ouvrir dans un navigateur pour inviter le bot.
