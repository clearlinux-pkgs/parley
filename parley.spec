#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : parley
Version  : 22.04.2
Release  : 43
URL      : https://download.kde.org/stable/release-service/22.04.2/src/parley-22.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.2/src/parley-22.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.2/src/parley-22.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 GPL-3.0 MIT
Requires: parley-bin = %{version}-%{release}
Requires: parley-data = %{version}-%{release}
Requires: parley-license = %{version}-%{release}
Requires: parley-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkeduvocdocument-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : qtwebengine-dev

%description
All files in this directory are copied from KDE/kdegames/libkdegames. Please avoid modifying the code in here and try go get changes back into kdegames.

%package bin
Summary: bin components for the parley package.
Group: Binaries
Requires: parley-data = %{version}-%{release}
Requires: parley-license = %{version}-%{release}

%description bin
bin components for the parley package.


%package data
Summary: data components for the parley package.
Group: Data

%description data
data components for the parley package.


%package doc
Summary: doc components for the parley package.
Group: Documentation

%description doc
doc components for the parley package.


%package license
Summary: license components for the parley package.
Group: Default

%description license
license components for the parley package.


%package locales
Summary: locales components for the parley package.
Group: Default

%description locales
locales components for the parley package.


%prep
%setup -q -n parley-22.04.2
cd %{_builddir}/parley-22.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1654821187
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1654821187
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/parley
cp %{_builddir}/parley-22.04.2/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/parley/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc
cp %{_builddir}/parley-22.04.2/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/parley/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/parley-22.04.2/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/parley/2123756e0b1fc8243547235a33c0fcabfe3b9a51
cp %{_builddir}/parley-22.04.2/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/parley/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/parley-22.04.2/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/parley/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/parley-22.04.2/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/parley/81e12d0c07782abcf558af7aa19846e3e2606a70
pushd clr-build
%make_install
popd
%find_lang parley

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/parley

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.parley.desktop
/usr/share/config.kcfg/documentsettings.kcfg
/usr/share/config.kcfg/languagesettings.kcfg
/usr/share/config.kcfg/parley.kcfg
/usr/share/icons/hicolor/128x128/apps/parley.png
/usr/share/icons/hicolor/16x16/apps/parley.png
/usr/share/icons/hicolor/32x32/apps/parley.png
/usr/share/icons/hicolor/48x48/apps/parley.png
/usr/share/icons/hicolor/64x64/apps/parley.png
/usr/share/icons/hicolor/scalable/apps/parley-parley.svgz
/usr/share/icons/hicolor/scalable/apps/parley-simple.svgz
/usr/share/icons/hicolor/scalable/apps/parley.svgz
/usr/share/icons/oxygen/16x16/actions/cards-block.png
/usr/share/icons/oxygen/16x16/actions/edit-entry.png
/usr/share/icons/oxygen/16x16/actions/edit-table-row.png
/usr/share/icons/oxygen/16x16/actions/lesson-add.png
/usr/share/icons/oxygen/16x16/actions/lesson-remove.png
/usr/share/icons/oxygen/16x16/actions/list-add-card.png
/usr/share/icons/oxygen/16x16/actions/list-remove-card.png
/usr/share/icons/oxygen/16x16/actions/multiple-choice.png
/usr/share/icons/oxygen/16x16/actions/practice-setup.png
/usr/share/icons/oxygen/16x16/actions/practice-start.png
/usr/share/icons/oxygen/16x16/actions/practice-stop.png
/usr/share/icons/oxygen/16x16/actions/remove-duplicates.png
/usr/share/icons/oxygen/16x16/actions/set-language.png
/usr/share/icons/oxygen/16x16/actions/specific-setup.png
/usr/share/icons/oxygen/22x22/actions/cards-block.png
/usr/share/icons/oxygen/22x22/actions/edit-entry.png
/usr/share/icons/oxygen/22x22/actions/edit-table-row.png
/usr/share/icons/oxygen/22x22/actions/lesson-add.png
/usr/share/icons/oxygen/22x22/actions/lesson-remove.png
/usr/share/icons/oxygen/22x22/actions/list-add-card.png
/usr/share/icons/oxygen/22x22/actions/list-remove-card.png
/usr/share/icons/oxygen/22x22/actions/multiple-choice.png
/usr/share/icons/oxygen/22x22/actions/practice-setup.png
/usr/share/icons/oxygen/22x22/actions/practice-start.png
/usr/share/icons/oxygen/22x22/actions/practice-stop.png
/usr/share/icons/oxygen/22x22/actions/remove-duplicates.png
/usr/share/icons/oxygen/22x22/actions/set-language.png
/usr/share/icons/oxygen/22x22/actions/specific-setup.png
/usr/share/icons/oxygen/32x32/actions/cards-block.png
/usr/share/icons/oxygen/32x32/actions/edit-entry.png
/usr/share/icons/oxygen/32x32/actions/edit-table-row.png
/usr/share/icons/oxygen/32x32/actions/lesson-add.png
/usr/share/icons/oxygen/32x32/actions/lesson-remove.png
/usr/share/icons/oxygen/32x32/actions/list-add-card.png
/usr/share/icons/oxygen/32x32/actions/list-remove-card.png
/usr/share/icons/oxygen/32x32/actions/multiple-choice.png
/usr/share/icons/oxygen/32x32/actions/practice-setup.png
/usr/share/icons/oxygen/32x32/actions/practice-start.png
/usr/share/icons/oxygen/32x32/actions/practice-stop.png
/usr/share/icons/oxygen/32x32/actions/remove-duplicates.png
/usr/share/icons/oxygen/32x32/actions/set-language.png
/usr/share/icons/oxygen/32x32/actions/specific-setup.png
/usr/share/icons/oxygen/48x48/actions/cards-block.png
/usr/share/icons/oxygen/48x48/actions/edit-entry.png
/usr/share/icons/oxygen/48x48/actions/edit-table-row.png
/usr/share/icons/oxygen/48x48/actions/lesson-add.png
/usr/share/icons/oxygen/48x48/actions/lesson-remove.png
/usr/share/icons/oxygen/48x48/actions/list-add-card.png
/usr/share/icons/oxygen/48x48/actions/list-remove-card.png
/usr/share/icons/oxygen/48x48/actions/multiple-choice.png
/usr/share/icons/oxygen/48x48/actions/practice-setup.png
/usr/share/icons/oxygen/48x48/actions/practice-start.png
/usr/share/icons/oxygen/48x48/actions/practice-stop.png
/usr/share/icons/oxygen/48x48/actions/remove-duplicates.png
/usr/share/icons/oxygen/48x48/actions/set-language.png
/usr/share/icons/oxygen/48x48/actions/specific-setup.png
/usr/share/icons/oxygen/scalable/actions/cards-block.svgz
/usr/share/icons/oxygen/scalable/actions/edit-entry.svgz
/usr/share/icons/oxygen/scalable/actions/edit-table-row.svgz
/usr/share/icons/oxygen/scalable/actions/lesson-add.svgz
/usr/share/icons/oxygen/scalable/actions/lesson-remove.svgz
/usr/share/icons/oxygen/scalable/actions/list-add-card.svgz
/usr/share/icons/oxygen/scalable/actions/list-remove-card.svgz
/usr/share/icons/oxygen/scalable/actions/practice-setup.svgz
/usr/share/icons/oxygen/scalable/actions/practice-start.svgz
/usr/share/icons/oxygen/scalable/actions/remove-duplicates.svgz
/usr/share/icons/oxygen/scalable/actions/set-language.svgz
/usr/share/icons/oxygen/scalable/actions/specific-setup.svgz
/usr/share/knsrcfiles/parley-themes.knsrc
/usr/share/knsrcfiles/parley.knsrc
/usr/share/kxmlgui5/parley/dashboardui.rc
/usr/share/kxmlgui5/parley/editorui.rc
/usr/share/kxmlgui5/parley/parleyui.rc
/usr/share/kxmlgui5/parley/practicesummaryui.rc
/usr/share/kxmlgui5/parley/practiceui.rc
/usr/share/kxmlgui5/parley/statisticsui.rc
/usr/share/kxmlgui5/parley/themes/bees_theme.desktop
/usr/share/kxmlgui5/parley/themes/bees_theme.svgz
/usr/share/kxmlgui5/parley/themes/bees_theme_preview.jpg
/usr/share/kxmlgui5/parley/themes/theme_reference.desktop
/usr/share/kxmlgui5/parley/themes/theme_reference.svgz
/usr/share/kxmlgui5/parley/themes/theme_reference_preview.jpg
/usr/share/metainfo/org.kde.parley.appdata.xml
/usr/share/parley/themes/bees_theme.desktop
/usr/share/parley/themes/bees_theme.svgz
/usr/share/parley/themes/bees_theme_preview.jpg
/usr/share/parley/themes/theme_reference.desktop
/usr/share/parley/themes/theme_reference.svgz
/usr/share/parley/themes/theme_reference_preview.jpg
/usr/share/parley/xslt/flashcards.xsl
/usr/share/parley/xslt/table.xsl

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/parley/index.cache.bz2
/usr/share/doc/HTML/ca/parley/index.docbook
/usr/share/doc/HTML/de/parley/Configure_blocking.png
/usr/share/doc/HTML/de/parley/Configure_practice.png
/usr/share/doc/HTML/de/parley/Configure_practice_conjugation.png
/usr/share/doc/HTML/de/parley/Folder_with_sound_and_pictures.png
/usr/share/doc/HTML/de/parley/Parley_articles_and_gender_0-9-4_001.png
/usr/share/doc/HTML/de/parley/Parley_articles_and_gender_0-9-4_002.png
/usr/share/doc/HTML/de/parley/Parley_articles_and_gender_0-9-4_003.png
/usr/share/doc/HTML/de/parley/Parley_comparison_eng-deu_0-9-4_002.png
/usr/share/doc/HTML/de/parley/Parley_comparison_eng-deu_0-9-4_003.png
/usr/share/doc/HTML/de/parley/Parley_configure_advanced.png
/usr/share/doc/HTML/de/parley/Parley_configure_parley_0-9-4_001.png
/usr/share/doc/HTML/de/parley/Parley_configure_parley_0-9-4_002.png
/usr/share/doc/HTML/de/parley/Parley_configure_parley_0-9-4_003.png
/usr/share/doc/HTML/de/parley/Parley_configure_parley_0-9-4_004.png
/usr/share/doc/HTML/de/parley/Parley_configure_thresholds.png
/usr/share/doc/HTML/de/parley/Parley_create_new_exercise_collective_names1.png
/usr/share/doc/HTML/de/parley/Parley_create_new_exercise_collective_names10.png
/usr/share/doc/HTML/de/parley/Parley_create_new_exercise_collective_names4.png
/usr/share/doc/HTML/de/parley/Parley_create_new_exercise_collective_names5.png
/usr/share/doc/HTML/de/parley/Parley_create_new_exercise_collective_names7.png
/usr/share/doc/HTML/de/parley/Parley_create_new_exercise_collective_names8.png
/usr/share/doc/HTML/de/parley/Parley_document_properties.png
/usr/share/doc/HTML/de/parley/Parley_edit_comparison_form_1.png
/usr/share/doc/HTML/de/parley/Parley_edit_comparison_form_2.png
/usr/share/doc/HTML/de/parley/Parley_edit_comparison_form_3.png
/usr/share/doc/HTML/de/parley/Parley_edit_conjugation_1.png
/usr/share/doc/HTML/de/parley/Parley_edit_conjugation_2.png
/usr/share/doc/HTML/de/parley/Parley_edit_main.png
/usr/share/doc/HTML/de/parley/Parley_file_select_dialog_0-9-4.png
/usr/share/doc/HTML/de/parley/Parley_get_new_stuff_0-9-4_001.png
/usr/share/doc/HTML/de/parley/Parley_initial_screen_0-9-4.png
/usr/share/doc/HTML/de/parley/Parley_mixed_letters_0-9-4_001.png
/usr/share/doc/HTML/de/parley/Parley_mixed_letters_0-9-4_002.png
/usr/share/doc/HTML/de/parley/Parley_mixed_letters_0-9-4_003.png
/usr/share/doc/HTML/de/parley/Parley_mixed_letters_0-9-4_004.png
/usr/share/doc/HTML/de/parley/Parley_multiple_choice_0-9-4_001.png
/usr/share/doc/HTML/de/parley/Parley_multiple_choice_0-9-4_002.png
/usr/share/doc/HTML/de/parley/Parley_multiple_choice_0-9-4_003.png
/usr/share/doc/HTML/de/parley/Parley_new_document_lang_articles.png
/usr/share/doc/HTML/de/parley/Parley_new_document_lang_general.png
/usr/share/doc/HTML/de/parley/Parley_new_document_lang_personalpronouns.png
/usr/share/doc/HTML/de/parley/Parley_new_document_lang_tenses.png
/usr/share/doc/HTML/de/parley/Parley_new_lesson1.png
/usr/share/doc/HTML/de/parley/Parley_new_lesson2.png
/usr/share/doc/HTML/de/parley/Parley_practice_bees.png
/usr/share/doc/HTML/de/parley/Parley_practice_conjugation.png
/usr/share/doc/HTML/de/parley/Parley_practice_fluffy.png
/usr/share/doc/HTML/de/parley/Parley_practice_grey_flash.png
/usr/share/doc/HTML/de/parley/Parley_practice_grey_flash_solution.png
/usr/share/doc/HTML/de/parley/Parley_practice_grey_written.png
/usr/share/doc/HTML/de/parley/Parley_practice_grey_written_right.png
/usr/share/doc/HTML/de/parley/Parley_practice_grey_written_wrong.png
/usr/share/doc/HTML/de/parley/Parley_practice_summary.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_001.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_002.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_003.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_004.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_005.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_006.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_007.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_008.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_009.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_010.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_011.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_012.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_013.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_014.png
/usr/share/doc/HTML/de/parley/Parley_trainer_eng-deu_0-9-4_015.png
/usr/share/doc/HTML/de/parley/Parley_welcome_screen.png
/usr/share/doc/HTML/de/parley/index.cache.bz2
/usr/share/doc/HTML/de/parley/index.docbook
/usr/share/doc/HTML/en/parley/Configure_practice_conjugation.png
/usr/share/doc/HTML/en/parley/Folder_with_sound_and_pictures.png
/usr/share/doc/HTML/en/parley/Parley_create_new_exercise_collective_names1.png
/usr/share/doc/HTML/en/parley/Parley_create_new_exercise_collective_names10.png
/usr/share/doc/HTML/en/parley/Parley_create_new_exercise_collective_names4.png
/usr/share/doc/HTML/en/parley/Parley_create_new_exercise_collective_names5.png
/usr/share/doc/HTML/en/parley/Parley_create_new_exercise_collective_names7.png
/usr/share/doc/HTML/en/parley/Parley_create_new_exercise_collective_names8.png
/usr/share/doc/HTML/en/parley/Parley_practice_conjugation.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_004.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_005.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_006.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_007.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_008.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_009.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_010.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_011.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_012.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_013.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_014.png
/usr/share/doc/HTML/en/parley/Parley_trainer_eng-deu_0-9-4_015.png
/usr/share/doc/HTML/en/parley/adding-images.png
/usr/share/doc/HTML/en/parley/adding-sound.png
/usr/share/doc/HTML/en/parley/articles_and_gender.png
/usr/share/doc/HTML/en/parley/articles_and_gender_right.png
/usr/share/doc/HTML/en/parley/articles_and_gender_wrong.png
/usr/share/doc/HTML/en/parley/comparison.png
/usr/share/doc/HTML/en/parley/comparison_form.png
/usr/share/doc/HTML/en/parley/comparison_form_edit.png
/usr/share/doc/HTML/en/parley/comparison_right.png
/usr/share/doc/HTML/en/parley/configure_blocking.png
/usr/share/doc/HTML/en/parley/configure_general.png
/usr/share/doc/HTML/en/parley/configure_generalconfig.png
/usr/share/doc/HTML/en/parley/configure_practice.png
/usr/share/doc/HTML/en/parley/configure_specific.png
/usr/share/doc/HTML/en/parley/configure_theme.png
/usr/share/doc/HTML/en/parley/configure_thresholds.png
/usr/share/doc/HTML/en/parley/configure_view.png
/usr/share/doc/HTML/en/parley/conjugation.png
/usr/share/doc/HTML/en/parley/conjugation_edit.png
/usr/share/doc/HTML/en/parley/dashboard.png
/usr/share/doc/HTML/en/parley/document-export.png
/usr/share/doc/HTML/en/parley/document_properties.png
/usr/share/doc/HTML/en/parley/edit_main.png
/usr/share/doc/HTML/en/parley/file_select_dialog.png
/usr/share/doc/HTML/en/parley/folder-black.png
/usr/share/doc/HTML/en/parley/general_document_properties.png
/usr/share/doc/HTML/en/parley/get_new_stuff.png
/usr/share/doc/HTML/en/parley/icon-delete.png
/usr/share/doc/HTML/en/parley/index.cache.bz2
/usr/share/doc/HTML/en/parley/index.docbook
/usr/share/doc/HTML/en/parley/initial_screen.png
/usr/share/doc/HTML/en/parley/lang_articles.png
/usr/share/doc/HTML/en/parley/lang_general.png
/usr/share/doc/HTML/en/parley/lang_personal_pronouns.png
/usr/share/doc/HTML/en/parley/lang_tenses.png
/usr/share/doc/HTML/en/parley/list-add-card.png
/usr/share/doc/HTML/en/parley/list-add.png
/usr/share/doc/HTML/en/parley/mixed_letters_hint.png
/usr/share/doc/HTML/en/parley/mixed_letters_right.png
/usr/share/doc/HTML/en/parley/mixed_letters_solution.png
/usr/share/doc/HTML/en/parley/mixed_letters_wrong.png
/usr/share/doc/HTML/en/parley/multiple_choice-right.png
/usr/share/doc/HTML/en/parley/multiple_choice-wrong.png
/usr/share/doc/HTML/en/parley/multiple_choice.png
/usr/share/doc/HTML/en/parley/new_empty_collection.png
/usr/share/doc/HTML/en/parley/new_lesson2.png
/usr/share/doc/HTML/en/parley/ocument-export.png
/usr/share/doc/HTML/en/parley/practice-setup.png
/usr/share/doc/HTML/en/parley/practice-start.png
/usr/share/doc/HTML/en/parley/practice_bees.png
/usr/share/doc/HTML/en/parley/practice_flash_solution.png
/usr/share/doc/HTML/en/parley/practice_grey.png
/usr/share/doc/HTML/en/parley/practice_summary.png
/usr/share/doc/HTML/en/parley/practice_written.png
/usr/share/doc/HTML/en/parley/practice_written_right.png
/usr/share/doc/HTML/en/parley/practice_written_wrong.png
/usr/share/doc/HTML/en/parley/save_new_collection.png
/usr/share/doc/HTML/en/parley/vocabulary_columns.png
/usr/share/doc/HTML/es/parley/index.cache.bz2
/usr/share/doc/HTML/es/parley/index.docbook
/usr/share/doc/HTML/it/parley/index.cache.bz2
/usr/share/doc/HTML/it/parley/index.docbook
/usr/share/doc/HTML/nl/parley/index.cache.bz2
/usr/share/doc/HTML/nl/parley/index.docbook
/usr/share/doc/HTML/pt/parley/index.cache.bz2
/usr/share/doc/HTML/pt/parley/index.docbook
/usr/share/doc/HTML/pt_BR/parley/index.cache.bz2
/usr/share/doc/HTML/pt_BR/parley/index.docbook
/usr/share/doc/HTML/ru/parley/index.cache.bz2
/usr/share/doc/HTML/ru/parley/index.docbook
/usr/share/doc/HTML/sv/parley/index.cache.bz2
/usr/share/doc/HTML/sv/parley/index.docbook
/usr/share/doc/HTML/uk/parley/index.cache.bz2
/usr/share/doc/HTML/uk/parley/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/parley/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/parley/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/parley/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/parley/81e12d0c07782abcf558af7aa19846e3e2606a70
/usr/share/package-licenses/parley/ee03d68f6be20b170e5ea5d114d6acafb3f2d1dc

%files locales -f parley.lang
%defattr(-,root,root,-)

