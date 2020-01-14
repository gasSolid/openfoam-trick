/*---------------------------------------------------------------------------*\
  =========                 |
  \\      /  F ield         | foam-extend: Open Source CFD
   \\    /   O peration     | Version:     4.0
    \\  /    A nd           | Web:         http://www.foam-extend.org
     \\/     M anipulation  | For copyright notice see file Copyright
-------------------------------------------------------------------------------
License
    This file is part of foam-extend.

    foam-extend is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or (at your
    option) any later version.

    foam-extend is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with foam-extend.  If not, see <http://www.gnu.org/licenses/>.

Application
    icoIbFoam

Description
    Transient solver for incompressible, laminar flow of Newtonian fluids
    with immersed boundary support.

Author
    Hrvoje Jasak, Wikki Ltd.  All rights reserved

\*---------------------------------------------------------------------------*/

#include "fvCFD.H"

// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

int main(int argc, char *argv[])
{
#   include "setRootCase.H"
#   include "createTime.H"
#   include "createMesh.H"

#   include "createFields.H"
#   include "smooth_field.h"
#   include "createFields_smooth_field.H"
vector test(vector::zero);
label celli = mesh.findCell(test);
Info<<"celli = "<<celli<<endl;
p[celli] = 1000;

p_smooth.internalField() = p.internalField();
smooth_field (p_smooth, diffusionRunTime, diffusionMesh,smoothFieldProperties);

Info<<"sum p_smooth = "<<sum(p_smooth)<<endl;

p_smooth.write();
p.write();

    return 0;
}


// ************************************************************************* //
