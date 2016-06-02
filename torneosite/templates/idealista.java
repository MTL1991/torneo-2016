List<UrbanizacionesID> findUrbanizacionesIDtoDrone(double lat,double lon,int range){
    
    List<UrbanizacionesIDs> IDsList = new ArrayList<UrbanizacionesIDs>();

    list.add(obtenerIdentificadorurbanizacion(lat,lon));
    UrbanizacionesID arribaAux = obtenerIdentificadorurbanizacion(lat,lon);
    UrbanizacionesID abajoAux = obtenerIdentificadorurbanizacion(lat,lon);

    for(int i=0;i<range;i++){
        list.add(obtenerAdyacente(arribaAux,ARRIBA));
        arribaAux = obtenerAdyacente(arribaAux,ARRIBA);
        obtenerAdyacente(abajoAux,ABAJO);
        abajoAux = obtenerAdyacente(abajoAux,ABAJO);

    }

    for(UrbanizacionesID origen : IDsList){
        
        UrbanizacionesID derechaAux = origen;
        UrbanizacionesID izquierdaAux = origen;

        for(int i=0;i<range;i++){
            list.add(obtenerAdyacente(derechaAux,DERECHA));
            derechaAux = obtenerAdyacente(derechaAux,DERECHA);
            obtenerAdyacente(izquierdaAux,IZQUIERDA);
            izquierdaAux = obtenerAdyacente(izquierdaAux,IZQUIERDA);
        }
    }

    return IDsList;

}
