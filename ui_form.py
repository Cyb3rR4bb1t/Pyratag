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
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QStatusBar, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1181, 894)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.top_panel = QHBoxLayout()
        self.top_panel.setObjectName(u"top_panel")
        self.current_dir_btn = QToolButton(self.centralwidget)
        self.current_dir_btn.setObjectName(u"current_dir_btn")
        self.current_dir_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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
        self.rename_combo.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.horizontalLayout_6.addWidget(self.rename_combo)

        self.rename_btn = QToolButton(self.widget_2)
        self.rename_btn.setObjectName(u"rename_btn")
        self.rename_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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
        self.verticalLayout_5.setContentsMargins(-1, 9, -1, 14)
        self.select_all_check = QCheckBox(self.groupBox)
        self.select_all_check.setObjectName(u"select_all_check")
        self.select_all_check.setCheckable(True)
        self.select_all_check.setTristate(False)

        self.verticalLayout_5.addWidget(self.select_all_check)

        self.files = QListWidget(self.groupBox)
        self.files.setObjectName(u"files")
        self.files.setEditTriggers(QAbstractItemView.EditTrigger.CurrentChanged|QAbstractItemView.EditTrigger.DoubleClicked|QAbstractItemView.EditTrigger.EditKeyPressed)
        self.files.setTabKeyNavigation(True)
        self.files.setDragDropMode(QAbstractItemView.DragDropMode.InternalMove)
        self.files.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.files.setAlternatingRowColors(False)
        self.files.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.files.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.files.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.files.setViewMode(QListView.ViewMode.ListMode)
        self.files.setUniformItemSizes(True)
        self.files.setSelectionRectVisible(True)
        self.files.setItemAlignment(Qt.AlignmentFlag.AlignLeading)
        self.files.setSupportedDragActions(Qt.DropAction.MoveAction)

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
        self.tabWidget_2.setIconSize(QSize(24, 24))
        self.tabWidget_2.setDocumentMode(True)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_24 = QVBoxLayout(self.tab_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.scrollArea_2 = QScrollArea(self.tab_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMinimumSize(QSize(400, 0))
        self.scrollArea_2.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollArea_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaContent_2 = QWidget()
        self.scrollAreaContent_2.setObjectName(u"scrollAreaContent_2")
        self.scrollAreaContent_2.setEnabled(True)
        self.scrollAreaContent_2.setGeometry(QRect(0, 0, 567, 733))
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollAreaContent_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaContent_2.setSizePolicy(sizePolicy5)
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaContent_2)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_9 = QSpacerItem(20, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.metadata_content_2 = QWidget(self.scrollAreaContent_2)
        self.metadata_content_2.setObjectName(u"metadata_content_2")
        self.metadata_content_2.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.metadata_content_2.sizePolicy().hasHeightForWidth())
        self.metadata_content_2.setSizePolicy(sizePolicy5)
        self.metadata_content_2.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_17 = QVBoxLayout(self.metadata_content_2)
        self.verticalLayout_17.setSpacing(6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.groupBox_4 = QGroupBox(self.metadata_content_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.dir_convention_combo = QComboBox(self.groupBox_4)
        self.dir_convention_combo.addItem("")
        self.dir_convention_combo.addItem("")
        self.dir_convention_combo.addItem("")
        self.dir_convention_combo.setObjectName(u"dir_convention_combo")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.dir_convention_combo)


        self.verticalLayout_12.addLayout(self.formLayout_2)


        self.verticalLayout_17.addWidget(self.groupBox_4)

        self.groupBox_3 = QGroupBox(self.metadata_content_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.detect_filesystem_group = QGroupBox(self.groupBox_3)
        self.detect_filesystem_group.setObjectName(u"detect_filesystem_group")
        self.detect_filesystem_group.setCheckable(True)
        self.verticalLayout_10 = QVBoxLayout(self.detect_filesystem_group)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_26 = QLabel(self.detect_filesystem_group)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_26)

        self.detect_title_combo = QComboBox(self.detect_filesystem_group)
        self.detect_title_combo.setObjectName(u"detect_title_combo")
        sizePolicy4.setHeightForWidth(self.detect_title_combo.sizePolicy().hasHeightForWidth())
        self.detect_title_combo.setSizePolicy(sizePolicy4)

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.detect_title_combo)

        self.label_25 = QLabel(self.detect_filesystem_group)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_25)

        self.detect_artist_combo = QComboBox(self.detect_filesystem_group)
        self.detect_artist_combo.setObjectName(u"detect_artist_combo")
        sizePolicy4.setHeightForWidth(self.detect_artist_combo.sizePolicy().hasHeightForWidth())
        self.detect_artist_combo.setSizePolicy(sizePolicy4)

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.FieldRole, self.detect_artist_combo)

        self.label_24 = QLabel(self.detect_filesystem_group)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_24)

        self.detect_album_combo = QComboBox(self.detect_filesystem_group)
        self.detect_album_combo.setObjectName(u"detect_album_combo")
        sizePolicy4.setHeightForWidth(self.detect_album_combo.sizePolicy().hasHeightForWidth())
        self.detect_album_combo.setSizePolicy(sizePolicy4)

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.FieldRole, self.detect_album_combo)


        self.verticalLayout_10.addLayout(self.formLayout_7)


        self.verticalLayout_4.addWidget(self.detect_filesystem_group)


        self.verticalLayout_17.addWidget(self.groupBox_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_2)


        self.horizontalLayout_12.addWidget(self.metadata_content_2)

        self.horizontalSpacer_17 = QSpacerItem(1, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_17)

        self.scrollArea_2.setWidget(self.scrollAreaContent_2)

        self.verticalLayout_24.addWidget(self.scrollArea_2)

        icon4 = QIcon()
        icon4.addFile(u":/icons/settings.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_2.addTab(self.tab_2, icon4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setEnabled(True)
        self.verticalLayout_8 = QVBoxLayout(self.tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea = QScrollArea(self.tab)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(400, 0))
        self.scrollArea.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.scrollArea.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaContent = QWidget()
        self.scrollAreaContent.setObjectName(u"scrollAreaContent")
        self.scrollAreaContent.setEnabled(True)
        self.scrollAreaContent.setGeometry(QRect(0, -42, 553, 766))
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
        self.tabWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)
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

        self.tag_cover_back = QLabel(self.back)
        self.tag_cover_back.setObjectName(u"tag_cover_back")
        self.tag_cover_back.setEnabled(True)
        self.tag_cover_back.setMinimumSize(QSize(250, 250))
        self.tag_cover_back.setMaximumSize(QSize(250, 250))
        self.tag_cover_back.setPixmap(QPixmap(u":/images/photo-scan.png"))
        self.tag_cover_back.setScaledContents(True)
        self.tag_cover_back.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tag_cover_back.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout_3.addWidget(self.tag_cover_back)

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

        self.tag_cover_front = QLabel(self.front)
        self.tag_cover_front.setObjectName(u"tag_cover_front")
        self.tag_cover_front.setEnabled(True)
        self.tag_cover_front.setMinimumSize(QSize(250, 250))
        self.tag_cover_front.setMaximumSize(QSize(250, 250))
        self.tag_cover_front.setPixmap(QPixmap(u":/images/photo-scan.png"))
        self.tag_cover_front.setScaledContents(True)
        self.tag_cover_front.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tag_cover_front.setTextInteractionFlags(Qt.TextInteractionFlag.NoTextInteraction)

        self.horizontalLayout.addWidget(self.tag_cover_front)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.front, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.cover_front_add = QToolButton(self.groupBox_2)
        self.cover_front_add.setObjectName(u"cover_front_add")
        self.cover_front_add.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.cover_front_add.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/icons/file-plus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cover_front_add.setIcon(icon5)
        self.cover_front_add.setIconSize(QSize(24, 24))
        self.cover_front_add.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.cover_front_add)

        self.front_cover_remove = QToolButton(self.groupBox_2)
        self.front_cover_remove.setObjectName(u"front_cover_remove")
        self.front_cover_remove.setEnabled(False)
        self.front_cover_remove.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon6 = QIcon()
        icon6.addFile(u":/icons/file-minus.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.front_cover_remove.setIcon(icon6)
        self.front_cover_remove.setIconSize(QSize(24, 24))
        self.front_cover_remove.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.front_cover_remove)

        self.cover_front_export = QToolButton(self.groupBox_2)
        self.cover_front_export.setObjectName(u"cover_front_export")
        self.cover_front_export.setEnabled(False)
        self.cover_front_export.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon7 = QIcon()
        icon7.addFile(u":/icons/download.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cover_front_export.setIcon(icon7)
        self.cover_front_export.setIconSize(QSize(24, 24))
        self.cover_front_export.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.cover_front_export)

        self.cover_front_info = QToolButton(self.groupBox_2)
        self.cover_front_info.setObjectName(u"cover_front_info")
        self.cover_front_info.setEnabled(False)
        self.cover_front_info.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon8 = QIcon()
        icon8.addFile(u":/icons/info-circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.cover_front_info.setIcon(icon8)
        self.cover_front_info.setIconSize(QSize(24, 24))
        self.cover_front_info.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout_11.addWidget(self.cover_front_info)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_7 = QGroupBox(self.metadata_content)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy6.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy6)
        self.verticalLayout = QVBoxLayout(self.groupBox_7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox_7)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.label_2 = QLabel(self.groupBox_7)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.tag_genre = QLineEdit(self.groupBox_7)
        self.tag_genre.setObjectName(u"tag_genre")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.tag_genre)

        self.label_6 = QLabel(self.groupBox_7)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.tag_year = QLineEdit(self.groupBox_7)
        self.tag_year.setObjectName(u"tag_year")
        self.tag_year.setMaxLength(4)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.tag_year)

        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_13)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)

        self.tag_track_num = QLineEdit(self.groupBox_7)
        self.tag_track_num.setObjectName(u"tag_track_num")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.tag_track_num.sizePolicy().hasHeightForWidth())
        self.tag_track_num.setSizePolicy(sizePolicy7)
        self.tag_track_num.setMinimumSize(QSize(50, 0))
        self.tag_track_num.setMaximumSize(QSize(50, 16777215))
        self.tag_track_num.setMaxLength(4)

        self.horizontalLayout_5.addWidget(self.tag_track_num)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.label_14)

        self.tag_track_total = QLineEdit(self.groupBox_7)
        self.tag_track_total.setObjectName(u"tag_track_total")
        sizePolicy7.setHeightForWidth(self.tag_track_total.sizePolicy().hasHeightForWidth())
        self.tag_track_total.setSizePolicy(sizePolicy7)
        self.tag_track_total.setMinimumSize(QSize(50, 0))
        self.tag_track_total.setMaximumSize(QSize(50, 16777215))
        self.tag_track_total.setBaseSize(QSize(0, 0))
        self.tag_track_total.setMaxLength(4)

        self.horizontalLayout_5.addWidget(self.tag_track_total)


        self.formLayout.setLayout(6, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_5)

        self.label_15 = QLabel(self.groupBox_7)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_15)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)

        self.tag_disk_num = QLineEdit(self.groupBox_7)
        self.tag_disk_num.setObjectName(u"tag_disk_num")
        sizePolicy7.setHeightForWidth(self.tag_disk_num.sizePolicy().hasHeightForWidth())
        self.tag_disk_num.setSizePolicy(sizePolicy7)
        self.tag_disk_num.setMinimumSize(QSize(50, 0))
        self.tag_disk_num.setMaximumSize(QSize(50, 16777215))
        self.tag_disk_num.setMaxLength(4)

        self.horizontalLayout_7.addWidget(self.tag_disk_num)

        self.label_16 = QLabel(self.groupBox_7)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.label_16)

        self.tag_disk_total = QLineEdit(self.groupBox_7)
        self.tag_disk_total.setObjectName(u"tag_disk_total")
        self.tag_disk_total.setMinimumSize(QSize(50, 0))
        self.tag_disk_total.setMaximumSize(QSize(50, 16777215))
        self.tag_disk_total.setMaxLength(4)

        self.horizontalLayout_7.addWidget(self.tag_disk_total)


        self.formLayout.setLayout(7, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.tag_album = QLineEdit(self.groupBox_7)
        self.tag_album.setObjectName(u"tag_album")

        self.horizontalLayout_9.addWidget(self.tag_album)

        self.detect_album_btn = QToolButton(self.groupBox_7)
        self.detect_album_btn.setObjectName(u"detect_album_btn")
        self.detect_album_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        icon9 = QIcon()
        icon9.addFile(u":/icons/wand.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.detect_album_btn.setIcon(icon9)
        self.detect_album_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.detect_album_btn)


        self.formLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tag_artist = QLineEdit(self.groupBox_7)
        self.tag_artist.setObjectName(u"tag_artist")

        self.horizontalLayout_2.addWidget(self.tag_artist)

        self.detect_artist_btn = QToolButton(self.groupBox_7)
        self.detect_artist_btn.setObjectName(u"detect_artist_btn")
        self.detect_artist_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.detect_artist_btn.setIcon(icon9)
        self.detect_artist_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.detect_artist_btn)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)

        self.tag_album_artist = QLineEdit(self.groupBox_7)
        self.tag_album_artist.setObjectName(u"tag_album_artist")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.tag_album_artist)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.tag_title = QLineEdit(self.groupBox_7)
        self.tag_title.setObjectName(u"tag_title")

        self.horizontalLayout_13.addWidget(self.tag_title)

        self.detect_title_btn = QToolButton(self.groupBox_7)
        self.detect_title_btn.setObjectName(u"detect_title_btn")
        self.detect_title_btn.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.detect_title_btn.setIcon(icon9)
        self.detect_title_btn.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.detect_title_btn)


        self.formLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_13)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_9.addWidget(self.groupBox_7)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_8.addWidget(self.metadata_content)

        self.horizontalSpacer_6 = QSpacerItem(1, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)

        self.scrollArea.setWidget(self.scrollAreaContent)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.line_3 = QFrame(self.tab)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_8.addWidget(self.line_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.apply_btn = QPushButton(self.tab)
        self.apply_btn.setObjectName(u"apply_btn")

        self.horizontalLayout_10.addWidget(self.apply_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.clear_btn = QPushButton(self.tab)
        self.clear_btn.setObjectName(u"clear_btn")

        self.horizontalLayout_10.addWidget(self.clear_btn)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_10.addWidget(self.pushButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_10)

        icon10 = QIcon()
        icon10.addFile(u":/icons/file-text.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_2.addTab(self.tab, icon10, "")

        self.right_panel.addWidget(self.tabWidget_2)

        self.splitter.addWidget(self.verticalLayoutWidget_2)

        self.verticalLayout_11.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1181, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.tabWidget_3, self.search_input)
        QWidget.setTabOrder(self.search_input, self.select_all_check)
        QWidget.setTabOrder(self.select_all_check, self.files)
        QWidget.setTabOrder(self.files, self.tabWidget_2)
        QWidget.setTabOrder(self.tabWidget_2, self.tag_title)
        QWidget.setTabOrder(self.tag_title, self.tag_artist)
        QWidget.setTabOrder(self.tag_artist, self.tag_album)
        QWidget.setTabOrder(self.tag_album, self.tag_album_artist)
        QWidget.setTabOrder(self.tag_album_artist, self.tag_genre)
        QWidget.setTabOrder(self.tag_genre, self.tag_year)
        QWidget.setTabOrder(self.tag_year, self.tag_track_num)
        QWidget.setTabOrder(self.tag_track_num, self.tag_track_total)
        QWidget.setTabOrder(self.tag_track_total, self.tag_disk_num)
        QWidget.setTabOrder(self.tag_disk_num, self.tag_disk_total)
        QWidget.setTabOrder(self.tag_disk_total, self.detect_title_combo)
        QWidget.setTabOrder(self.detect_title_combo, self.detect_artist_combo)
        QWidget.setTabOrder(self.detect_artist_combo, self.detect_album_combo)

        self.retranslateUi(MainWindow)

        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.dir_convention_combo.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.current_dir_btn.setText(QCoreApplication.translate("MainWindow", u"Select directory", None))
        self.current_dir_view.setInputMask("")
        self.current_dir_view.setText("")
        self.current_dir_view.setPlaceholderText(QCoreApplication.translate("MainWindow", u"path", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Rename files to:", None))
        self.rename_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"Title.ext", None))
        self.rename_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Track Title.ext", None))
        self.rename_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Disk-Track Title.ext", None))
        self.rename_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"Artist - Title.ext", None))
        self.rename_combo.setItemText(4, QCoreApplication.translate("MainWindow", u"Track Artist - Title.ext", None))
        self.rename_combo.setItemText(5, QCoreApplication.translate("MainWindow", u"Disk-Track Artist - Title.ext", None))

        self.rename_btn.setText(QCoreApplication.translate("MainWindow", u"Rename files", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), "")
        self.search_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), "")
        self.groupBox.setTitle("")
        self.select_all_check.setText(QCoreApplication.translate("MainWindow", u"Select all", None))
        self.files_selection_count.setText(QCoreApplication.translate("MainWindow", u"0 of 2 selected", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"General", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Default Directory convention", None))
        self.dir_convention_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.dir_convention_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"Album/", None))
        self.dir_convention_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"Artist/Album/", None))

        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Detect button behavior", None))
        self.detect_filesystem_group.setTitle(QCoreApplication.translate("MainWindow", u"set tag from filesystem", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Title (file)", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Artist (directory)", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Album (directory)", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), "")
#if QT_CONFIG(tooltip)
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Detection Settings", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Cover", None))
        self.tag_cover_back.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.back), QCoreApplication.translate("MainWindow", u"Back", None))
        self.tag_cover_front.setText("")
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
        self.tag_track_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"num", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.tag_track_total.setPlaceholderText(QCoreApplication.translate("MainWindow", u"total", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.tag_disk_num.setPlaceholderText(QCoreApplication.translate("MainWindow", u"num", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.tag_disk_total.setPlaceholderText(QCoreApplication.translate("MainWindow", u"total", None))
#if QT_CONFIG(tooltip)
        self.detect_album_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Detect Album", None))
#endif // QT_CONFIG(tooltip)
        self.detect_album_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.detect_artist_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Detect Artist", None))
#endif // QT_CONFIG(tooltip)
        self.detect_artist_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
#if QT_CONFIG(tooltip)
        self.detect_title_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Detect Title", None))
#endif // QT_CONFIG(tooltip)
        self.detect_title_btn.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.apply_btn.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Restore", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), "")
#if QT_CONFIG(tooltip)
        self.tabWidget_2.setTabToolTip(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Audio file Metadata", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

