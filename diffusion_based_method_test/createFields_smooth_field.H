// 2019/12/27 14:51:47 smooth field zhaopeng


    Foam::Time diffusionRunTime
         (
         "controlDiffDict",
         runTime.rootPath(),
         runTime.caseName()
         );
    fvMesh diffusionMesh
            (
             Foam::IOobject
             (
              Foam::fvMesh::defaultRegion,
              diffusionRunTime.timeName(),
              diffusionRunTime,
              Foam::IOobject::MUST_READ
             )
            );
    IOdictionary smoothFieldProperties
            (
             IOobject
             (
              "smoothFieldProperties",
              runTime.constant(),
              mesh,
              IOobject::MUST_READ,
              IOobject::NO_WRITE
             )
            );

