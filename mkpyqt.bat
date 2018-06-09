@ECHO OFF
REM generate resource file
CD well_pygeopressure
pyrcc4.exe -o ui/resources_rc.py resources.qrc

REM generate ui file
CD ui
CALL pyuic4.bat -o ui_main_window.py main_window.ui
CALL pyuic4.bat -o ui_survey_edit.py survey_edit.ui
CALL pyuic4.bat -o ui_survey_select.py survey_select.ui
CALL pyuic4.bat -o ui_well_manage_dialog.py well_manage_dialog.ui
CALL pyuic4.bat -o ui_well_marker_dialog.py well_marker_dialog.ui
CALL pyuic4.bat -o ui_import_multiple_wells_dialog.py import_multiple_wells_dialog.ui
CALL pyuic4.bat -o ui_read_multiple_wells_from_file_dialog.py read_multiple_wells_from_file_dialog.ui
CALL pyuic4.bat -o ui_format_definition_dialog.py format_definition_dialog.ui
CALL pyuic4.bat -o ui_import_logs_dialog.py import_logs_dialog.ui
REM Tools
CALL pyuic4.bat -o ui_smooth_dialog.py smooth_dialog.ui
CALL pyuic4.bat -o ui_upscale_dialog.py upscale_dialog.ui
CALL pyuic4.bat -o ui_discern_shale_dialog.py discern_shale_dialog.ui
CALL pyuic4.bat -o ui_extrapolate_dialog.py extrapolate_dialog.ui
CALL pyuic4.bat -o ui_obp_dialog.py obp_dialog.ui
CALL pyuic4.bat -o ui_nct_dialog.py nct_dialog.ui
CALL pyuic4.bat -o ui_optimize_eaton_dialog.py optimize_eaton_dialog.ui
CALL pyuic4.bat -o ui_eaton_dialog.py eaton_dialog.ui
CALL pyuic4.bat -o ui_optimize_bowers_dialog.py optimize_bowers_dialog.ui
CALL pyuic4.bat -o ui_bowers_dialog.py bowers_dialog.ui
CD ..\..
REM python app.py
