# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QFormLayout, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTabWidget, QToolButton,
    QVBoxLayout, QWidget)
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.top_panel = QHBoxLayout()
        self.top_panel.setObjectName(u"top_panel")
        self.current_dir_btn = QToolButton(self.centralwidget)
        self.current_dir_btn.setObjectName(u"current_dir_btn")
        icon = QIcon()
        icon.addFile(u":/icons/folder.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.current_dir_btn.setIcon(icon)
        self.current_dir_btn.setIconSize(QSize(24, 24))
        self.current_dir_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.top_panel.addWidget(self.current_dir_btn)

        self.current_dir_view = QLineEdit(self.centralwidget)
        self.current_dir_view.setObjectName(u"current_dir_view")
        self.current_dir_view.setEnabled(True)
        self.current_dir_view.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.current_dir_view.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.current_dir_view.setAcceptDrops(False)
        self.current_dir_view.setMaxLength(32767)
        self.current_dir_view.setReadOnly(True)
        self.current_dir_view.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.current_dir_view.setClearButtonEnabled(False)

        self.top_panel.addWidget(self.current_dir_view)


        self.verticalLayout_11.addLayout(self.top_panel)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(False)
        self.left_panel = QWidget(self.splitter)
        self.left_panel.setObjectName(u"left_panel")
        self.left_panel.setMaximumSize(QSize(700, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.left_panel)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_3 = QTabWidget(self.left_panel)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy1)
        self.tabWidget_3.setMinimumSize(QSize(250, 0))
        self.tabWidget_3.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tabWidget_3.setDocumentMode(True)
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_14 = QVBoxLayout(self.tab_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, 0, 0)
        self.widget_2 = QWidget(self.tab_4)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.widget_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.rename_combo = QComboBox(self.widget_2)
        self.rename_combo.addItem("")
        self.rename_combo.addItem("")
        self.rename_combo.addItem("")
        self.rename_combo.addItem("")
        self.rename_combo.addItem("")
        self.rename_combo.addItem("")
        self.rename_combo.setObjectName(u"rename_combo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.rename_combo.sizePolicy().hasHeightForWidth())
        self.rename_combo.setSizePolicy(sizePolicy4)
        self.rename_combo.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_6.addWidget(self.rename_combo)

        self.rename_btn = QToolButton(self.widget_2)
        self.rename_btn.setObjectName(u"rename_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/pencil-bolt.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.rename_btn.setIcon(icon1)
        self.rename_btn.setIconSize(QSize(24, 24))
        self.rename_btn.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.horizontalLayout_6.addWidget(self.rename_btn)


        self.verticalLayout_14.addWidget(self.widget_2)

        icon2 = QIcon()
        icon2.addFile(u":/icons/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_3.addTab(self.tab_4, icon2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_13 = QVBoxLayout(self.tab_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, -1, 0, 0)
        self.widget = QWidget(self.tab_3)
        self.widget.setObjectName(u"widget")
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_16 = QVBoxLayout(self.widget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.search_input = QLineEdit(self.widget)
        self.search_input.setObjectName(u"search_input")
        self.search_input.setMinimumSize(QSize(0, 0))
        self.search_input.setClearButtonEnabled(True)

        self.verticalLayout_16.addWidget(self.search_input)


        self.verticalLayout_13.addWidget(self.widget)

        icon3 = QIcon()
        icon3.addFile(u":/icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_3.addTab(self.tab_3, icon3, "")

        self.verticalLayout_3.addWidget(self.tabWidget_3)

        self.groupBox = QGroupBox(self.left_panel)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 9, -1, 5)
        self.select_all_check = QCheckBox(self.groupBox)
        self.select_all_check.setObjectName(u"select_all_check")
        self.select_all_check.setCheckable(True)
        self.select_all_check.setTristate(False)

        self.verticalLayout_5.addWidget(self.select_all_check)

        self.files = QListWidget(self.groupBox)
        self.files.setObjectName(u"files")
        self.files.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)

        self.verticalLayout_5.addWidget(self.files)

        self.line = QFrame(self.groupBox)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.files_selection_count = QLabel(self.groupBox)
        self.files_selection_count.setObjectName(u"files_selection_count")
        self.files_selection_count.setEnabled(False)

        self.verticalLayout_5.addWidget(self.files_selection_count)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.splitter.addWidget(self.left_panel)
        self.verticalLayoutWidget_2 = QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.right_panel = QVBoxLayout(self.verticalLayoutWidget_2)
        self.right_panel.setObjectName(u"right_panel")
        self.right_panel.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.verticalLayoutWidget_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tabWidget_2.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(400, 0))
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContent = QWidget()
        self.scrollAreaContent.setObjectName(u"scrollAreaContent")
        self.scrollAreaContent.setEnabled(True)
        self.scrollAreaContent.setGeometry(QRect(0, 0, 419, 894))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollAreaContent.sizePolicy().hasHeightForWidth())
        self.scrollAreaContent.setSizePolicy(sizePolicy5)
        self.horizontalLayout_8 = QHBoxLayout(self.scrollAreaContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)

        self.metadata_content = QWidget(self.scrollAreaContent)
        self.metadata_content.setObjectName(u"metadata_content")
        self.metadata_content.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.metadata_content.sizePolicy().hasHeightForWidth())
        self.metadata_content.setSizePolicy(sizePolicy5)
        self.metadata_content.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_9 = QVBoxLayout(self.metadata_content)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_2 = QGroupBox(self.metadata_content)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy6)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy6.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy6)
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.back = QWidget()
        self.back.setObjectName(u"back")
        self.back.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_7 = QVBoxLayout(self.back)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.cover_back_view = QLabel(self.back)
        self.cover_back_view.setObjectName(u"cover_back_view")
        self.cover_back_view.setEnabled(True)
        self.cover_back_view.setMinimumSize(QSize(250, 250))
        self.cover_back_view.setMaximumSize(QSize(250, 250))
        self.cover_back_view.setPixmap(QPixmap(u":/images/photo-scan.png"))
        self.cover_back_view.setScaledContents(True)
        self.cover_back_view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover_back_view.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.cover_back_view)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.back, "")
        self.front = QWidget()
        self.front.setObjectName(u"front")
        self.front.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_6 = QVBoxLayout(self.front)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.cover_front_view = QLabel(self.front)
        self.cover_front_view.setObjectName(u"cover_front_view")
        self.cover_front_view.setEnabled(True)
        self.cover_front_view.setMinimumSize(QSize(250, 250))
        self.cover_front_view.setMaximumSize(QSize(250, 250))
        self.cover_front_view.setPixmap(QPixmap(u":/images/photo-scan.png"))
        self.cover_front_view.setScaledContents(True)
        self.cover_front_view.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cover_front_view.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout.addWidget(self.cover_front_view)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.front, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cover_front_add = QToolButton(self.groupBox_2)
        self.cover_front_add.setObjectName(u"cover_front_add")
        self.cover_front_add.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/icons/file-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cover_front_add.setIcon(icon4)
        self.cover_front_add.setIconSize(QSize(24, 24))
        self.cover_front_add.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.cover_front_add)

        self.front_cover_remove = QToolButton(self.groupBox_2)
        self.front_cover_remove.setObjectName(u"front_cover_remove")
        self.front_cover_remove.setEnabled(False)
        icon5 = QIcon()
        icon5.addFile(u":/icons/file-minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.front_cover_remove.setIcon(icon5)
        self.front_cover_remove.setIconSize(QSize(24, 24))
        self.front_cover_remove.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.front_cover_remove)

        self.cover_front_export = QToolButton(self.groupBox_2)
        self.cover_front_export.setObjectName(u"cover_front_export")
        self.cover_front_export.setEnabled(False)
        icon6 = QIcon()
        icon6.addFile(u":/icons/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cover_front_export.setIcon(icon6)
        self.cover_front_export.setIconSize(QSize(24, 24))
        self.cover_front_export.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.cover_front_export)

        self.cover_front_info = QToolButton(self.groupBox_2)
        self.cover_front_info.setObjectName(u"cover_front_info")
        self.cover_front_info.setEnabled(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/info-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cover_front_info.setIcon(icon7)
        self.cover_front_info.setIconSize(QSize(24, 24))
        self.cover_front_info.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.cover_front_info)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_7 = QGroupBox(self.metadata_content)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy6.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy6)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.prop_title = QLineEdit(self.groupBox_7)
        self.prop_title.setObjectName(u"prop_title")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.prop_title)

        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.prop_album_artist = QLineEdit(self.groupBox_7)
        self.prop_album_artist.setObjectName(u"prop_album_artist")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.prop_album_artist)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.prop_genre = QLineEdit(self.groupBox_7)
        self.prop_genre.setObjectName(u"prop_genre")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.prop_genre)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.prop_year = QLineEdit(self.groupBox_7)
        self.prop_year.setObjectName(u"prop_year")
        self.prop_year.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.prop_year.setMaxLength(4)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.prop_year)

        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.prop_track_num = QLineEdit(self.groupBox_7)
        self.prop_track_num.setObjectName(u"prop_track_num")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.prop_track_num.sizePolicy().hasHeightForWidth())
        self.prop_track_num.setSizePolicy(sizePolicy7)
        self.prop_track_num.setMinimumSize(QSize(50, 0))
        self.prop_track_num.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_5.addWidget(self.prop_track_num)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.prop_track_total = QLineEdit(self.groupBox_7)
        self.prop_track_total.setObjectName(u"prop_track_total")
        sizePolicy7.setHeightForWidth(self.prop_track_total.sizePolicy().hasHeightForWidth())
        self.prop_track_total.setSizePolicy(sizePolicy7)
        self.prop_track_total.setMinimumSize(QSize(50, 0))
        self.prop_track_total.setMaximumSize(QSize(50, 16777215))
        self.prop_track_total.setBaseSize(QSize(0, 0))

        self.horizontalLayout_5.addWidget(self.prop_track_total)


        self.formLayout.setLayout(6, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_5)

        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.prop_disk_num = QLineEdit(self.groupBox_7)
        self.prop_disk_num.setObjectName(u"prop_disk_num")
        sizePolicy7.setHeightForWidth(self.prop_disk_num.sizePolicy().hasHeightForWidth())
        self.prop_disk_num.setSizePolicy(sizePolicy7)
        self.prop_disk_num.setMinimumSize(QSize(50, 0))
        self.prop_disk_num.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_7.addWidget(self.prop_disk_num)

        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.label_16)

        self.prop_disk_total = QLineEdit(self.groupBox_7)
        self.prop_disk_total.setObjectName(u"prop_disk_total")
        self.prop_disk_total.setMinimumSize(QSize(50, 0))
        self.prop_disk_total.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_7.addWidget(self.prop_disk_total)


        self.formLayout.setLayout(7, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.prop_album = QLineEdit(self.groupBox_7)
        self.prop_album.setObjectName(u"prop_album")

        self.horizontalLayout_9.addWidget(self.prop_album)

        self.detect_album_btn = QToolButton(self.groupBox_7)
        self.detect_album_btn.setObjectName(u"detect_album_btn")
        icon8 = QIcon()
        icon8.addFile(u":/icons/wand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.detect_album_btn.setIcon(icon8)
        self.detect_album_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.detect_album_btn)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.prop_artist = QLineEdit(self.groupBox_7)
        self.prop_artist.setObjectName(u"prop_artist")

        self.horizontalLayout_2.addWidget(self.prop_artist)

        self.detect_artist_btn = QToolButton(self.groupBox_7)
        self.detect_artist_btn.setObjectName(u"detect_artist_btn")
        self.detect_artist_btn.setIcon(icon8)
        self.detect_artist_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.detect_artist_btn)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)


        self.verticalLayout_12.addLayout(self.formLayout)


        self.verticalLayout_9.addWidget(self.groupBox_7)

        self.groupBox_3 = QGroupBox(self.metadata_content)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setCheckable(False)
        self.groupBox_3.setChecked(False)
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget_4 = QTabWidget(self.groupBox_3)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tab_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_15 = QVBoxLayout(self.tab_6)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_10 = QLabel(self.tab_6)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.detect_album_combo = QComboBox(self.tab_6)
        self.detect_album_combo.addItem("")
        self.detect_album_combo.addItem("")
        self.detect_album_combo.setObjectName(u"detect_album_combo")
        sizePolicy4.setHeightForWidth(self.detect_album_combo.sizePolicy().hasHeightForWidth())
        self.detect_album_combo.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.detect_album_combo)


        self.verticalLayout_15.addLayout(self.formLayout_3)

        self.tabWidget_4.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tab_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.verticalLayout_10 = QVBoxLayout(self.tab_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_9)

        self.detect_artist_combo = QComboBox(self.tab_5)
        self.detect_artist_combo.addItem("")
        self.detect_artist_combo.addItem("")
        self.detect_artist_combo.setObjectName(u"detect_artist_combo")
        sizePolicy4.setHeightForWidth(self.detect_artist_combo.sizePolicy().hasHeightForWidth())
        self.detect_artist_combo.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.detect_artist_combo)


        self.verticalLayout_10.addLayout(self.formLayout_2)

        self.tabWidget_4.addTab(self.tab_5, "")

        self.verticalLayout.addWidget(self.tabWidget_4)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_8.addWidget(self.metadata_content)

        self.horizontalSpacer_6 = QSpacerItem(1, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.scrollArea.setWidget(self.scrollAreaContent)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.tabWidget_2.addTab(self.tab, "")

        self.right_panel.addWidget(self.tabWidget_2)

        self.line_3 = QFrame(self.verticalLayoutWidget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.right_panel.addWidget(self.line_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.clear_btn = QPushButton(self.verticalLayoutWidget_2)
        self.clear_btn.setObjectName(u"clear_btn")

        self.horizontalLayout_10.addWidget(self.clear_btn)

        self.apply_btn = QPushButton(self.verticalLayoutWidget_2)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout_10.addWidget(self.apply_btn)


        self.right_panel.addLayout(self.horizontalLayout_10)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_11.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.current_dir_btn.setText(QCoreApplication.translate("MainWindow", u"Select directory", None))
        self.current_dir_view.setInputMask("")
        self.current_dir_view.setText("")
        self.current_dir_view.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rename files to:", None))
        self.rename_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"<title>.ext", None))
        self.rename_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"<number> - <title>.ext", None))
        self.rename_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"<disk>-<number> - <title>.ext", None))
        self.rename_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"<title> - <artist>.ext", None))
        self.rename_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"<number> - <title> - <artist>.ext", None))
        self.rename_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"<disk>-<number> - <title> - <artist>.ext", None))

        self.rename_btn.setText(QCoreApplication.translate("MainWindow", u"Rename files", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), "")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), "")
        self.groupBox.setTitle("")
        self.select_all_check.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
        self.files_selection_count.setText(QCoreApplication.translate("MainWindow", u"0 of 2 selected", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Additional", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Cover", None))
        self.cover_back_view.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.back), QCoreApplication.translate("MainWindow", u"Back", None))
        self.cover_front_view.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.front), QCoreApplication.translate("MainWindow", u"Front", None))
        self.cover_front_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.front_cover_remove.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.cover_front_export.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.cover_front_info.setText(QCoreApplication.translate("MainWindow", u"Info", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Artist", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Album", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Album Artist", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Track", None))
        self.prop_track_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"num", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.prop_track_total.setPlaceholderText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.prop_disk_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"num", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.prop_disk_total.setPlaceholderText(QCoreApplication.translate("MainWindow", u"total", None))
        self.detect_album_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.detect_artist_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"From directory", None))
        self.detect_album_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"parent", None))
        self.detect_album_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"grandparent", None))

        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Album", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"From directory", None))
        self.detect_artist_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"grandparent", None))
        self.detect_artist_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"parent", None))

        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Artist", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Metadata", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
    # retranslateUi

