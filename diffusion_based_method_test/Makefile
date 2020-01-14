
#----------------- dir of OpenFOAM----------------------
#dir where you install OF
FOAM_DIR := /opt/OpenFOAM/OpenFOAM-2.3.x
FOAM_LIB_DIR := $(FOAM_DIR)/platforms/linux64IccDPOpt/lib
FOAM_LIB_DIR2 := $(FOAM_DIR)/platforms/linux64IccDPOpt/lib/4.1.1.036

#----------------- cpp file compiler-------------------
mpidir := /opt/intel/impi/4.1.1.036
MPICC := $(mpidir)/bin64/mpicxx
CLDFLAGS := -lm -lnsl
mpiinc := $(mpidir)/include64
CINCLUDES := -I. -I$(mpiinc)
CC := $(MPICC) -fPIC 

CFLAGS := -m64 -Dlinux64 -DWM_DP -Wall -Wextra -Wno-unused-parameter -Wnon-virtual-dtor -O3 -DNoRepository -ftemplate-depth-100 

#--------------- openFOAM include files and libs------
FOAM_SRC	:= $(FOAM_DIR)/src
FOAM_SOLVER := $(FOAM_DIR)/applications/solvers

# included head files
POSIX := $(FOAM_SRC)/OSspecific/POSIX/lnInclude  
OpenFOAM := $(FOAM_SRC)/OpenFOAM/lnInclude
finiteVolume := $(FOAM_SRC)/finiteVolume/lnInclude
cfdTools := $(FOAM_SRC)/finiteVolume/cfdTools
interPhase := interfacialModels/lnInclude
phaseModel := phaseModel/lnInclude
kineticTheoryModels := kineticTheoryModels/lnInclude
		

# different models
bubbleFoam := $(FOAM_SOLVER)/multiphase/bubbleFoam
turbulenceModel	:= $(FOAM_SRC)/turbulenceModels/incompressible/turbulenceModel
#turbulenceModel_comp := $(FOAM_SRC)/turbulenceModels/compressible/turbulenceModel
transportModels	:= $(FOAM_SRC)/transportModels
#transportModels_comp := $(FOAM_SRC)/transportModels/compressible/lnInclude
transportModels_genel := $(FOAM_SRC)/transportModels/incompressible/transportModel
transportModels_single := $(FOAM_SRC)/transportModels/incompressible/singlePhaseTransportModel
meshSearch := $(FOAM_SRC)/meshTools/meshSearch
meshTools := $(FOAM_SRC)/meshTools/lnInclude
reaction := $(FOAM_SRC)/fvOptions/lnInclude
sampling := $(FOAM_SRC)/sampling/lnInclude
specie := $(FOAM_SRC)thermophysicalModels/specie/lnInclude
thermoModel :=$(FOAM_SRC)/thermophysicalModels/basic/lnInclude
triSurface := $(FOAM_SRC)/triSurface/lnInclude

CINCLUDES := -I. -I$(OpenFOAM) \
	-I$(POSIX) \
	-I$(finiteVolume) \
	-I$(cfdTools) \
	-I$(interPhase) \
	-I$(phaseModel) \
	-I$(transportModels_single) \
	-I$(kineticTheoryModels) \
	-I$(transportModels) \
	-I$(bubbleFoam) \
	-I$(turbulenceModel) \
	-I$(transportModels_genel) \
	-I$(meshSearch) \
	-I$(meshTools) \
	-I$(reaction) \
	-I$(sampling) \
	-I$(thermoModel) \
	-I$(turbulenceModel_comp) \
	-I$(transportModels_comp) \
	-I$(specie) \
	-I$(triSurface) \
	-I$(IBM)


CLDFLAGS := -L$(FOAM_LIB_DIR) -L$(FOAM_LIB_DIR2) -L$(FOAM_USER_LIBBIN) \
	-lOpenFOAM \
	-lPstream \
	-ldl \
	-lm \
	-lfiniteVolume \
	-lmeshTools \
	-lincompressibleTransportModels \
	-lincompressibleTurbulenceModel \
	-lincompressibleRASModels \
	-lincompressibleLESModels \
	-lfluidThermophysicalModels \
	-ltriSurface \
	-ldynamicMesh \
	-lsurfMesh \
	-lspecie \
	-lsampling \
	-lfileFormats \
	-lLESdeltas \
	-ltwoPhaseMixture \
	-lLESfilters \
	-lfvOptions \
	-lthermophysicalFunctions \

# obj files
OBJ_CPP_FILES := icoFoam.o \
				 smooth_field.o

OBJ_FILES := $(OBJ_CPP_FILES)

# link app
LINK := $(CC) -Xlinker --add-needed -Xlinker --no-as-needed 


exec_name := icoFoam

$(exec_name):$(OBJ_FILES) 
	$(LINK) -o $(exec_name) $(OBJ_FILES) $(CLDFLAGS)  $(CINCLUDES) $(CFLAGS) $(NVCCLDFLAGS)

# compile objs

icoFoam.o:icoFoam.C
	$(CC) -c icoFoam.C -o icoFoam.o $(CINCLUDES) $(CFLAGS)
smooth_field.o:smooth_field.cpp
	$(CC) -c smooth_field.cpp -o smooth_field.o $(CINCLUDES) $(CFLAGS)


clean:
	rm -f $(exec_name) $(OBJ_FILES)
