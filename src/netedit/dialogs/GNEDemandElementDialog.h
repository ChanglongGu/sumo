/****************************************************************************/
// Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
// Copyright (C) 2001-2019 German Aerospace Center (DLR) and others.
// This program and the accompanying materials
// are made available under the terms of the Eclipse Public License v2.0
// which accompanies this distribution, and is available at
// http://www.eclipse.org/legal/epl-v20.html
// SPDX-License-Identifier: EPL-2.0
/****************************************************************************/
/// @file    GNEDemandElementDialog.h
/// @author  Pablo Alvarez Lopez
/// @date    Jan 2018
/// @version $Id$
///
// A abstract class for editing additional elements
/****************************************************************************/
#ifndef GNEDemandElementDialog_h
#define GNEDemandElementDialog_h

// ===========================================================================
// included modules
// ===========================================================================

#include <config.h>

#include <fx.h>
#include <vector>
#include <utils/xml/SUMOXMLDefinitions.h>

// ===========================================================================
// class declarations
// ===========================================================================

class GNEDemandElement;
class GNEUndoList;

// ===========================================================================
// class definitions
// ===========================================================================

/**
 * @class GNEDemandElementDialog
 * @brief Dialog to edit sequences, parameters, etc.. of DemandElements
 */
class GNEDemandElementDialog : protected FXTopWindow {
    /// @brief FOX-declaration abstract
    FXDECLARE_ABSTRACT(GNEDemandElementDialog)

public:
    /// @brief constructor
    GNEDemandElementDialog(GNEDemandElement* parent, bool updatingElement, int width, int height);

    /// @brief destructor
    ~GNEDemandElementDialog();

    /// @brief get edited DemandElement
    GNEDemandElement* getEditedDemandElement() const;

    /// @name FOX-callbacks
    /// @{
    /// @brief event after press accept button
    virtual long onCmdAccept(FXObject* sender, FXSelector sel, void* ptr) = 0;

    /// @brief event after press cancel button
    virtual long onCmdCancel(FXObject* sender, FXSelector sel, void* ptr) = 0;

    /// @brief event after press cancel button
    virtual long onCmdReset(FXObject*, FXSelector, void*) = 0;

    /// @brief event after press a key
    long onKeyPress(FXObject* sender, FXSelector sel, void* ptr);

    /// @brief event after release a key
    long onKeyRelease(FXObject* sender, FXSelector sel, void* ptr);

    /// @}

protected:
    FOX_CONSTRUCTOR(GNEDemandElementDialog)

    /// @brief pointer to edited aditional
    GNEDemandElement* myEditedDemandElement;

    /// @brief flag to indicate if additional are being created or modified (cannot be changed after open dialog)
    bool myUpdatingElement;

    /// @brief frame for contents
    FXVerticalFrame* myContentFrame;

    /// @brief execute dialog as modal
    FXint openAsModalDialog(FXuint placement = PLACEMENT_CURSOR);

    /// @brief change additional dialog header
    void changeDemandElementDialogHeader(const std::string& newHeader);

    /// @brief init a new group of changes that will be do it in dialog
    void initChanges();

    /// @brief Accept changes did in this dialog.
    void acceptChanges();

    /// @brief Cancel changes did in this dialog.
    void cancelChanges();

    /// @brief reset changes did in this dialog.
    void resetChanges();

private:
    /// @brief accept button
    FXButton* myAcceptButton;

    /// @brief cancel button
    FXButton* myCancelButton;

    /// @brief cancel button
    FXButton* myResetButton;

    /// @brief description of changes did in this additional dialog
    std::string myChangesDescription;

    /// @brief number of GNEChanges_... in dialog
    int myNumberOfChanges;

    /// @brief Invalidated copy constructor
    GNEDemandElementDialog(const GNEDemandElementDialog&) = delete;

    /// @brief Invalidated assignment operator
    GNEDemandElementDialog& operator=(const GNEDemandElementDialog&) = delete;
};

#endif
