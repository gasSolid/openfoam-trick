// 2019/12/26 17:11:55 
// this code was used to smooth the volScalarField volVectorField for CFD-DEM with adaptive method 
// reference is Sun(2016): https://www.sciencedirect.com/science/article/pii/S0098300416300218


void smooth_field (volVectorField & sFieldIn, Time & diffusionRunTime_, fvMesh & diffusionMesh_,
                    IOdictionary& smoothFieldProperties); 
void smooth_field (volScalarField & sFieldIn, Time & diffusionRunTime_, fvMesh & diffusionMesh_,
                    IOdictionary& smoothFieldProperties); 
