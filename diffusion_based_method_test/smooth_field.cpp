// 2019/12/26 17:11:55 
// this code was used to smooth the volScalarField volVectorField for CFD-DEM with adaptive method 
// reference is Sun(2016): https://www.sciencedirect.com/science/article/pii/S0098300416300218

# include "fvCFD.H"
# include "smooth_field.h"
void smooth_field (volVectorField & sFieldIn, Time & diffusionRunTime_, fvMesh & diffusionMesh_,
                    IOdictionary& smoothFieldProperties){ 
        volVectorField diffWorkField
    (
        IOobject
        (
            "tempDiffVector",
            diffusionRunTime_.timeName(),
            diffusionMesh_,
            IOobject::NO_READ,
            IOobject::NO_WRITE
        ),
        diffusionMesh_,
        dimensionedVector
        (
            "zero",
            dimless,
            vector::zero
        ),
        zeroGradientFvPatchVectorField::typeName
    );

    diffWorkField.internalField() = sFieldIn.internalField();

    tensor smoothDirection_ = smoothFieldProperties.lookupOrDefault
    (
        "smoothDirection",
        tensor(1.0, 0, 0, 0, 1.0, 0, 0, 0, 1.0)
    ); 
    scalar diffusionBandWidth(readScalar(smoothFieldProperties.lookup("diffusionBandWidth")));
    scalar diffusionSteps(readScalar(smoothFieldProperties.lookup("diffusionSteps")));

    // determine the time and time step in diffusion procedure
    scalar diffusionTime = pow(diffusionBandWidth, 2)/4;
    scalar diffusionDeltaT = diffusionTime/(diffusionSteps + SMALL);

    diffusionRunTime_.setEndTime(diffusionTime);
    diffusionRunTime_.setDeltaT(diffusionDeltaT);
    Info << "diffusion time is: " << diffusionTime << endl;
    Info << "diffusion time step is: " << diffusionDeltaT << endl;

    dimensionedTensor DT("DT", dimensionSet(0, 2, -1, 0, 0), smoothDirection_); 
    scalar startTime = diffusionRunTime_.startTimeIndex();
    label startIndex = diffusionRunTime_.timeIndex();

    Info<< "smoothing " << sFieldIn.name() << endl;

    while (diffusionRunTime_.loop())
    {
       /* if (diffusionRunTime_.timeIndex() == 1)
        {
            while (simple_.correctNonOrthogonal())
            {
                solve(fvm::ddt(diffWorkField) - fvm::laplacian(DT, diffWorkField));
            }
        }
        else
        {
            solve(fvm::ddt(diffWorkField) - fvm::laplacian(DT, diffWorkField));
        }*/
            solve(fvm::ddt(diffWorkField) - fvm::laplacian(DT, diffWorkField));
    }

    diffusionRunTime_.setTime(startTime,startIndex);

    sFieldIn.internalField() = diffWorkField.internalField();
}

void smooth_field (volScalarField & sFieldIn, Time & diffusionRunTime_, fvMesh & diffusionMesh_,
                    IOdictionary& smoothFieldProperties){ 
        volScalarField diffWorkField
    (
        IOobject
        (
            "tempDiffScalar",
            diffusionRunTime_.timeName(),
            diffusionMesh_,
            IOobject::NO_READ,
            IOobject::NO_WRITE
        ),
        diffusionMesh_,
        dimensionedScalar
        (
            "0",
            dimless,
            0.0
        ),
        zeroGradientFvPatchScalarField::typeName
    );

    diffWorkField.internalField() = sFieldIn.internalField();

    tensor smoothDirection_ = smoothFieldProperties.lookupOrDefault
    (
        "smoothDirection",
        tensor(1.0, 0, 0, 0, 1.0, 0, 0, 0, 1.0)
    ); 
    scalar diffusionBandWidth(readScalar(smoothFieldProperties.lookup("diffusionBandWidth")));
    scalar diffusionSteps(readScalar(smoothFieldProperties.lookup("diffusionSteps")));

    // determine the time and time step in diffusion procedure
    scalar diffusionTime = pow(diffusionBandWidth, 2)/4;
    scalar diffusionDeltaT = diffusionTime/(diffusionSteps + SMALL);

    diffusionRunTime_.setEndTime(diffusionTime);
    diffusionRunTime_.setDeltaT(diffusionDeltaT);
    Info << "diffusion time is: " << diffusionTime << endl;
    Info << "diffusion time step is: " << diffusionDeltaT << endl;

    dimensionedTensor DT("DT", dimensionSet(0, 2, -1, 0, 0), smoothDirection_); 
    scalar startTime = diffusionRunTime_.startTimeIndex();
    label startIndex = diffusionRunTime_.timeIndex();

    Info<< "smoothing " << sFieldIn.name() << endl;

    while (diffusionRunTime_.loop())
    {
            solve(fvm::ddt(diffWorkField) - fvm::laplacian(DT, diffWorkField));
    }

    diffusionRunTime_.setTime(startTime,startIndex);

    sFieldIn.internalField() = diffWorkField.internalField();
}

