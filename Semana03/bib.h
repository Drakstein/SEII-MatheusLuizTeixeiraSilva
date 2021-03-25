//MATHEUS LUIZ TEIXEIRA SILVA 11311EMT025

int funcsomaR(int real1,int real2){  
    int real = real1 + real2;
    return real;
}

int funcsomaI(int img1,int img2){  
    int img = img1 + img2;
    return img;
}

int funcsubR(int real1,int real2){  
    int real = real1 - real2;
    return real;
}

int funcsubI(int img1,int img2){  
    int img = img1 - img2;
return img;
}

int funcmultR(int real1,int img1,int real2,int img2){
int real = real1*real2 - img1*img2;
return real;
}

int funcmultI(int real1,int img1,int real2,int img2){
int img = real1*img2 + img1*real2;
return img;
}

int funcdivR(int real1,int img1,int real2,int img2){
int real = ((real1*real2) + (img1*img2));
return real;
}

int funcdivI(int real1,int img1,int real2,int img2){
int img = ((real2*img1) - (real1*img2));
return img;
}

int funcdivDen(int real2,int img2){
int den = ((real2*real2) + (img2*img2));
return den;
}