#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : parley
Version  : 19.08.3
Release  : 14
URL      : https://download.kde.org/stable/applications/19.08.3/src/parley-19.08.3.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.3/src/parley-19.08.3.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.3/src/parley-19.08.3.tar.xz.sig
Summary  : Vocabulary Trainer
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 ISC MIT
Requires: parley-bin = %{version}-%{release}
Requires: parley-data = %{version}-%{release}
Requires: parley-license = %{version}-%{release}
Requires: parley-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kross-dev
BuildRequires : libkeduvocdocument-dev
BuildRequires : libxml2-dev
BuildRequires : libxslt-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtwebengine-dev

%description
# Parley
Parley is a vocabulary trainer.
## Introduction
arley is a vocabulary trainer. It helps you to memorize your vocabulary, for example when you are trying to learn a foreign language. It supports many language specific features, but can be used for other learning tasks as well. It uses the spaced repetition learning method, which makes learning optimal. Vocabulary collections can be downloaded by "Get Hot New Stuff" or created with the built-in editor.

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
%setup -q -n parley-19.08.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573195474
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1573195474
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/parley
cp %{_builddir}/parley-19.08.3/COPYING %{buildroot}/usr/share/package-licenses/parley/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/parley-19.08.3/COPYING.DOC %{buildroot}/usr/share/package-licenses/parley/1bd373e4851a93027ba70064bd7dbdc6827147e1
cp %{_builddir}/parley-19.08.3/plugins/wiktionary/mwclient/LICENSE.md %{buildroot}/usr/share/package-licenses/parley/e4388e326ad32baa550534d43f340cf950d8a056
cp %{_builddir}/parley-19.08.3/plugins/wiktionary/mwclient/requests_oauthlib/LICENSE %{buildroot}/usr/share/package-licenses/parley/44d0ccfd43c5941abf44e8e5dba5e198a1b4badd
cp %{_builddir}/parley-19.08.3/plugins/wiktionary/mwclient/six.LICENSE %{buildroot}/usr/share/package-licenses/parley/f226af67862c0c7a0e921e24672a3a1375691e3e
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
/usr/share/parley/plugins/example.desktop
/usr/share/parley/plugins/example.py
/usr/share/parley/plugins/google_dictionary.desktop
/usr/share/parley/plugins/google_dictionary.py
/usr/share/parley/plugins/leo-dict.desktop
/usr/share/parley/plugins/leo-dict.py
/usr/share/parley/plugins/mwclient/LICENSE.md
/usr/share/parley/plugins/mwclient/README.rst
/usr/share/parley/plugins/mwclient/__init__.py
/usr/share/parley/plugins/mwclient/client.py
/usr/share/parley/plugins/mwclient/errors.py
/usr/share/parley/plugins/mwclient/ex.py
/usr/share/parley/plugins/mwclient/image.py
/usr/share/parley/plugins/mwclient/listing.py
/usr/share/parley/plugins/mwclient/page.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/__init__.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/__init__.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/douban.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/facebook.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/fitbit.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/linkedin.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/mailchimp.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/slack.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/compliance_fixes/weibo.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/oauth1_auth.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/oauth1_session.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/oauth2_auth.py
/usr/share/parley/plugins/mwclient/requests_oauthlib/oauth2_session.py
/usr/share/parley/plugins/mwclient/six.LICENSE
/usr/share/parley/plugins/mwclient/six.README
/usr/share/parley/plugins/mwclient/six.py
/usr/share/parley/plugins/mwclient/sleep.py
/usr/share/parley/plugins/mwclient/util.py
/usr/share/parley/plugins/wiktionary_sound.desktop
/usr/share/parley/plugins/wiktionary_sound.py
/usr/share/parley/themes/bees_theme.desktop
/usr/share/parley/themes/bees_theme.svgz
/usr/share/parley/themes/bees_theme_preview.jpg
/usr/share/parley/themes/theme_reference.desktop
/usr/share/parley/themes/theme_reference.svgz
/usr/share/parley/themes/theme_reference_preview.jpg
/usr/share/parley/tips
/usr/share/parley/xslt/flashcards.xsl
/usr/share/parley/xslt/table.xsl
/usr/share/xdg/parley-themes.knsrc
/usr/share/xdg/parley.knsrc

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
/usr/share/doc/HTML/en/parley/Parley_practice_icon_right.png
/usr/share/doc/HTML/en/parley/Parley_practice_icon_wrong.png
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
/usr/share/doc/HTML/en/parley/configure_parley.png
/usr/share/doc/HTML/en/parley/configure_practice.png
/usr/share/doc/HTML/en/parley/configure_specific.png
/usr/share/doc/HTML/en/parley/configure_theme.png
/usr/share/doc/HTML/en/parley/configure_thresholds.png
/usr/share/doc/HTML/en/parley/configure_view.png
/usr/share/doc/HTML/en/parley/conjugation.png
/usr/share/doc/HTML/en/parley/conjugation_edit.png
/usr/share/doc/HTML/en/parley/dashboard.png
/usr/share/doc/HTML/en/parley/document_properties.png
/usr/share/doc/HTML/en/parley/edit_main.png
/usr/share/doc/HTML/en/parley/file_select_dialog.png
/usr/share/doc/HTML/en/parley/general_document_properties.png
/usr/share/doc/HTML/en/parley/get_new_stuff.png
/usr/share/doc/HTML/en/parley/index.cache.bz2
/usr/share/doc/HTML/en/parley/index.docbook
/usr/share/doc/HTML/en/parley/initial_screen.png
/usr/share/doc/HTML/en/parley/lang_articles.png
/usr/share/doc/HTML/en/parley/lang_general.png
/usr/share/doc/HTML/en/parley/lang_personal_pronouns.png
/usr/share/doc/HTML/en/parley/lang_tenses.png
/usr/share/doc/HTML/en/parley/mixed_letters_hint.png
/usr/share/doc/HTML/en/parley/mixed_letters_right.png
/usr/share/doc/HTML/en/parley/mixed_letters_solution.png
/usr/share/doc/HTML/en/parley/mixed_letters_wrong.png
/usr/share/doc/HTML/en/parley/multiple_choice-right.png
/usr/share/doc/HTML/en/parley/multiple_choice-wrong.png
/usr/share/doc/HTML/en/parley/multiple_choice.png
/usr/share/doc/HTML/en/parley/new_empty_collection.png
/usr/share/doc/HTML/en/parley/new_lesson1.png
/usr/share/doc/HTML/en/parley/new_lesson2.png
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
/usr/share/doc/HTML/sv/parley/index.cache.bz2
/usr/share/doc/HTML/sv/parley/index.docbook
/usr/share/doc/HTML/uk/parley/index.cache.bz2
/usr/share/doc/HTML/uk/parley/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/parley/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/parley/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/parley/44d0ccfd43c5941abf44e8e5dba5e198a1b4badd
/usr/share/package-licenses/parley/e4388e326ad32baa550534d43f340cf950d8a056
/usr/share/package-licenses/parley/f226af67862c0c7a0e921e24672a3a1375691e3e

%files locales -f parley.lang
%defattr(-,root,root,-)

