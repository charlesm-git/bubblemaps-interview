# Test technique Bubblemaps

## Design Architecture

Le dossier `/architecture_design/` contient une capture d'écran ainsi qu'un lien vers un diagramme réalisé sur LucidChart. Des commentaires ont été ajoutés sur le diagramme pour facilité sa lisibilité et ajouter des précisions.

## API Python

L'API FastAPI est déployée sur Google Cloud Platform à l'adresse : https://bubblemaps-interview-api-948104408177.europe-west9.run.app  
  
Afin de répondre au besoin, deux endpoints ont été créés:  
* `/pool/{chainId}/{tokenAddress}`
    - Prend un couple chain/token en entrée et retourne pour ce token : la plus grosse pool, la liquidité total sur l'ensemble des pools, le nombre total de pool
    - exemple : `/pool/solana/FQgtfugBdpFN7PZ6NdPrZpVLDBrPGxXesi4gVu3vErhY`
* `/pools/{chainId}/{tokenAddresses}`
    - S'appuie sur le même principe que le premier endpoint mais pour plusieurs tokens d'une même chain.
    - Les adresses de token doivent être fournies sous la forme d'une chaine de caractères séparées par des virgules. Ne pas mettre d'espaces.  
    - exemple : `/pools/solana/FQgtfugBdpFN7PZ6NdPrZpVLDBrPGxXesi4gVu3vErhY,JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN`


L'API s'appuie sur l'API DexScanner. Elle supporte toutes blockchains et tokens. Cependant, ces derniers doivent être disponible via l'API DexScanner.
