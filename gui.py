import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton,
    QMessageBox,
    QFrame,
)

from PySide6.QtCore import Qt, QTimer

from job_parser import extract_job_details
from portfolio import Portfolio
from email_generator import generate_email


class ColdEmailGenerator(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Cold Email Generator")
        self.resize(1200, 750)

        # Load portfolio database
        self.portfolio = Portfolio()
        self.portfolio.load_portfolio()

        self.setup_ui()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(25, 20, 25, 20)
        main_layout.setSpacing(15)

        # ---------------- HEADER ----------------

        title = QLabel("AI Cold Email Generator")
        title.setAlignment(Qt.AlignCenter)
        title.setObjectName("title")

        subtitle = QLabel(
            "Generate personalized cold emails from job descriptions "
            "using AI and relevant portfolio projects."
        )
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setObjectName("subtitle")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # ---------------- MAIN CONTENT ----------------

        content_layout = QHBoxLayout()
        content_layout.setSpacing(20)

        # ================= LEFT PANEL =================

        left_panel = QFrame()
        left_panel.setObjectName("panel")

        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(15, 15, 15, 15)
        left_layout.setSpacing(10)

        jd_label = QLabel("Job Description")
        jd_label.setObjectName("sectionTitle")

        self.job_input = QTextEdit()
        self.job_input.setPlaceholderText(
            "Paste the complete job description here..."
        )

        # Generate + Clear buttons
        left_button_layout = QHBoxLayout()

        self.generate_button = QPushButton("Generate Cold Email")
        self.generate_button.setObjectName("generateButton")
        self.generate_button.clicked.connect(self.generate_email)

        self.clear_button = QPushButton("Clear All")
        self.clear_button.setObjectName("clearButton")
        self.clear_button.clicked.connect(self.clear_all)

        left_button_layout.addWidget(self.generate_button, 3)
        left_button_layout.addWidget(self.clear_button, 1)

        left_layout.addWidget(jd_label)
        left_layout.addWidget(self.job_input)
        left_layout.addLayout(left_button_layout)

        # ================= RIGHT PANEL =================

        right_panel = QFrame()
        right_panel.setObjectName("panel")

        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(15, 15, 15, 15)
        right_layout.setSpacing(8)

        # -------- Job Analysis --------

        analysis_label = QLabel("Job Analysis")
        analysis_label.setObjectName("sectionTitle")

        self.job_analysis = QTextEdit()
        self.job_analysis.setReadOnly(True)
        self.job_analysis.setPlaceholderText(
            "Extracted role, experience and skills will appear here..."
        )
        self.job_analysis.setMaximumHeight(135)

        # -------- Portfolio --------

        projects_label = QLabel("Matched Portfolio Projects")
        projects_label.setObjectName("sectionTitle")

        self.projects_output = QTextEdit()
        self.projects_output.setReadOnly(True)
        self.projects_output.setPlaceholderText(
            "Relevant portfolio projects will appear here..."
        )
        self.projects_output.setMaximumHeight(150)

        # -------- Generated Email --------

        email_label = QLabel("Generated Cold Email")
        email_label.setObjectName("sectionTitle")

        self.email_output = QTextEdit()
        self.email_output.setReadOnly(True)
        self.email_output.setPlaceholderText(
            "Your personalized cold email will appear here..."
        )

        # -------- Status --------

        self.status_label = QLabel("Ready")
        self.status_label.setObjectName("statusLabel")

        # -------- Copy Button --------

        self.copy_button = QPushButton("Copy Email")
        self.copy_button.setObjectName("copyButton")
        self.copy_button.clicked.connect(self.copy_email)

        right_layout.addWidget(analysis_label)
        right_layout.addWidget(self.job_analysis)

        right_layout.addWidget(projects_label)
        right_layout.addWidget(self.projects_output)

        right_layout.addWidget(email_label)
        right_layout.addWidget(self.email_output)

        right_layout.addWidget(self.status_label)
        right_layout.addWidget(self.copy_button)

        # Panel sizes
        content_layout.addWidget(left_panel, 4)
        content_layout.addWidget(right_panel, 6)

        main_layout.addLayout(content_layout)

        # ================= STYLING =================

        self.setStyleSheet(
            """
            QMainWindow {
                background-color: #0f172a;
            }

            QWidget {
                font-family: Segoe UI;
                font-size: 14px;
            }

            QLabel#title {
                color: white;
                font-size: 28px;
                font-weight: bold;
            }

            QLabel#subtitle {
                color: #94a3b8;
                font-size: 14px;
                margin-bottom: 10px;
            }

            QLabel#sectionTitle {
                color: #e2e8f0;
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 3px;
            }

            QLabel#statusLabel {
                color: #94a3b8;
                font-size: 12px;
                padding: 3px;
            }

            QFrame#panel {
                background-color: #1e293b;
                border: 1px solid #334155;
                border-radius: 12px;
            }

            QTextEdit {
                background-color: #0f172a;
                color: #e2e8f0;
                border: 1px solid #334155;
                border-radius: 8px;
                padding: 10px;
            }

            QTextEdit:focus {
                border: 1px solid #3b82f6;
            }

            QPushButton {
                min-height: 42px;
                border-radius: 8px;
                font-weight: bold;
                padding: 5px 15px;
            }

            QPushButton#generateButton {
                background-color: #2563eb;
                color: white;
                border: none;
            }

            QPushButton#generateButton:hover {
                background-color: #1d4ed8;
            }

            QPushButton#generateButton:disabled {
                background-color: #475569;
                color: #cbd5e1;
            }

            QPushButton#clearButton {
                background-color: #334155;
                color: #e2e8f0;
                border: 1px solid #475569;
            }

            QPushButton#clearButton:hover {
                background-color: #475569;
            }

            QPushButton#copyButton {
                background-color: #334155;
                color: white;
                border: 1px solid #475569;
            }

            QPushButton#copyButton:hover {
                background-color: #475569;
            }
            """
        )

    # ================= GENERATE EMAIL =================

    def generate_email(self):

        job_description = self.job_input.toPlainText().strip()

        if not job_description:
            QMessageBox.warning(
                self,
                "Missing Job Description",
                "Please paste a job description first."
            )
            return

        try:

            self.generate_button.setText("Generating...")
            self.generate_button.setEnabled(False)
            self.clear_button.setEnabled(False)

            self.status_label.setText(
                "Analyzing job description and generating email..."
            )

            QApplication.processEvents()

            # Extract job information
            job = extract_job_details(job_description)

            # Retrieve relevant portfolio projects
            links = self.portfolio.query_links(job["skills"])

            # Generate cold email
            email = generate_email(job, links)

            # ---------------- JOB ANALYSIS ----------------

            skills = ", ".join(job["skills"])

            analysis = (
                f"Role: {job['role']}\n"
                f"Experience: {job['experience']}\n"
                f"Skills: {skills}"
            )

            self.job_analysis.setPlainText(analysis)

            # ---------------- PORTFOLIO ----------------

            project_text = ""

            for project in links:

                project_text += (
                    f"{project['project']}\n"
                    f"Tech Stack: "
                    f"{project.get('techstack', 'N/A')}\n"
                    f"GitHub: {project['link']}\n\n"
                )

            self.projects_output.setPlainText(
                project_text.strip()
            )

            # ---------------- EMAIL ----------------

            self.email_output.setPlainText(email)

            self.status_label.setText(
                "Email generated successfully."
            )

        except Exception as error:

            self.status_label.setText(
                "Generation failed."
            )

            QMessageBox.critical(
                self,
                "Error",
                f"Something went wrong:\n\n{str(error)}"
            )

        finally:

            self.generate_button.setText(
                "Generate Cold Email"
            )

            self.generate_button.setEnabled(True)
            self.clear_button.setEnabled(True)

    # ================= COPY EMAIL =================

    def copy_email(self):

        email = self.email_output.toPlainText().strip()

        if not email:

            QMessageBox.information(
                self,
                "No Email",
                "Generate an email first."
            )

            return

        QApplication.clipboard().setText(email)

        self.copy_button.setText("Copied!")
        self.status_label.setText(
            "Email copied to clipboard."
        )

        # Automatically reset button after 1.5 seconds
        QTimer.singleShot(
            1500,
            self.reset_copy_button
        )

    def reset_copy_button(self):

        self.copy_button.setText("Copy Email")

    # ================= CLEAR =================

    def clear_all(self):

        self.job_input.clear()
        self.job_analysis.clear()
        self.projects_output.clear()
        self.email_output.clear()

        self.status_label.setText("Ready")
        self.copy_button.setText("Copy Email")

        self.job_input.setFocus()


# ================= START APPLICATION =================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ColdEmailGenerator()
    window.show()

    sys.exit(app.exec())