import streamlit as st 
import PyPDF2
import pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# nltk.download('stopwords')

st.title("Resume Screening Application")

st.subheader("NLP Based Resume Screening")

st.caption("By, ")
st.caption("Atharva Kapade ----- Lisshika Shetty ----- Jaskaran Singh Chawla")

# st.caption("Aim of this project is to check whether a candidate is qualified for a role based his or her education, experience, and other information captured on their resume. In a nutshell, it's a form of pattern matching between a job's requirements and the qualifications of a candidate based on their resume.")

uploadedJD = st.file_uploader("Upload Job Description", type="pdf")

uploadedResume = st.file_uploader("Upload resume",type="pdf")

click = st.button("Process")



try:
    global job_description
    with pdfplumber.open(uploadedJD) as pdf:
        pages = pdf.pages[0]
        job_description = pages.extract_text()
        job_description = re.sub('http\S+\s*', ' ', job_description)  # remove URLs
        job_description = re.sub('RT|cc', ' ', job_description)  # remove RT and cc
        job_description = re.sub('#\S+', '', job_description)  # remove hashtags
        job_description = re.sub('@\S+', '  ', job_description)  # remove mentions
        job_description = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', job_description)  # remove punctuations
        job_description = re.sub(r'[^\x00-\x7f]',r' ', job_description) 
        job_description = re.sub('\s+', ' ', job_description)  # remove extra whitespace

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(job_description)
        w = 1
        job_description_filtered_sentence1 = [w for w in word_tokens if not w in stop_words]
        job_description_filtered_sentence1 = ''
        job_description_filtered_sentence1list = []
        for w in word_tokens:
            if w not in stop_words:
                job_description_filtered_sentence1 += w + ' '
                job_description_filtered_sentence1list.append(w)
        #         print(word_tokens)
        # print(filtered_sentence1)
        # job_description = cleanResume(job_description)

except:
    st.write("")
    
    
try:
    global resume
    with  pdfplumber.open(uploadedResume) as pdf:
        pages = pdf.pages[0]
        resume = pages.extract_text()
        resume = re.sub('http\S+\s*', ' ', resume)  # remove URLs
        resume = re.sub('RT|cc', ' ', resume)  # remove RT and cc
        resume = re.sub('#\S+', '', resume)  # remove hashtags
        resume = re.sub('@\S+', '  ', resume)  # remove mentions
        resume = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resume)  # remove punctuations
        resume = re.sub(r'[^\x00-\x7f]',r' ', resume) 
        resume = re.sub('\s+', ' ', resume)  # remove extra whitespace

        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(resume)
        w = 1
        resume_filtered_sentence1 = [w for w in word_tokens if not w in stop_words]
        resume_filtered_sentence1 = ''
        resume_filtered_sentence1list = []
        for w in word_tokens:
            if w not in stop_words:
                resume_filtered_sentence1 += w + ' '
                resume_filtered_sentence1list.append(w)

        ds_keyword = ['tensorflow','keras','pytorch','machine learning','deep Learning','flask','streamlit', 'numpy', 
                      'hadoop', 'tableau', 'aws']
        web_keyword = ['react', 'django', 'node jS', 'react js', 'php', 'laravel', 'magento', 'wordpress',
                               'javascript', 'angular js', 'c#', 'flask']
        android_keyword = ['android','android development','flutter','kotlin','xml','kivy']
        ios_keyword = ['ios','ios development','swift','cocoa','cocoa touch','xcode']
        uiux_keyword = ['ux','adobe xd','figma','zeplin','balsamiq','ui','prototyping','wireframes','storyframes',
                        'adobe photoshop','photoshop','editing','adobe illustrator','illustrator','adobe after effects',
                        'after effects','adobe premier pro','premier pro','adobe indesign','indesign','wireframe','solid',
                        'grasp','user research','user experience']
        
        recommended_skills = []
        reco_field = ''
        rec_course = ''
        for i in resume_filtered_sentence1list:
            if i.lower() in ds_keyword:
                reco_field = 'Data Science'
            elif i.lower() in web_keyword:
                reco_field = 'Web Development'
            elif i.lower() in android_keyword:
                reco_field = 'Android Development'
            elif i.lower() in ios_keyword:
                reco_field = 'IOS Development'
            elif i.lower() in uiux_keyword:
                reco_field = 'UI-UX Development'

        ds_course = [['Machine Learning Crash Course by Google [Free]', 'https://developers.google.com/machine-learning/crash-course'],
             ['Machine Learning A-Z by Udemy','https://www.udemy.com/course/machinelearning/'],
             ['Machine Learning by Andrew NG','https://www.coursera.org/learn/machine-learning'],
             ['Data Scientist Master Program of Simplilearn (IBM)','https://www.simplilearn.com/big-data-and-analytics/senior-data-scientist-masters-program-training'],
             ['Data Science Foundations: Fundamentals by LinkedIn','https://www.linkedin.com/learning/data-science-foundations-fundamentals-5'],
             ['Data Scientist with Python','https://www.datacamp.com/tracks/data-scientist-with-python'],
             ['Programming for Data Science with Python','https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104'],
             ['Programming for Data Science with R','https://www.udacity.com/course/programming-for-data-science-nanodegree-with-R--nd118'],
             ['Introduction to Data Science','https://www.udacity.com/course/introduction-to-data-science--cd0017'],
             ['Intro to Machine Learning with TensorFlow','https://www.udacity.com/course/intro-to-machine-learning-with-tensorflow-nanodegree--nd230']]

        web_course = [['Django Crash course [Free]','https://youtu.be/e1IyzVyrLSU'],
                    ['Python and Django Full Stack Web Developer Bootcamp','https://www.udemy.com/course/python-and-django-full-stack-web-developer-bootcamp'],
                    ['React Crash Course [Free]','https://youtu.be/Dorf8i6lCuk'],
                    ['ReactJS Project Development Training','https://www.dotnettricks.com/training/masters-program/reactjs-certification-training'],
                    ['Full Stack Web Developer - MEAN Stack','https://www.simplilearn.com/full-stack-web-developer-mean-stack-certification-training'],
                    ['Node.js and Express.js [Free]','https://youtu.be/Oe421EPjeBE'],
                    ['Flask: Develop Web Applications in Python','https://www.educative.io/courses/flask-develop-web-applications-in-python'],
                    ['Full Stack Web Developer by Udacity','https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044'],
                    ['Front End Web Developer by Udacity','https://www.udacity.com/course/front-end-web-developer-nanodegree--nd0011'],
                    ['Become a React Developer by Udacity','https://www.udacity.com/course/react-nanodegree--nd019']]

        android_course = [['Android Development for Beginners [Free]','https://youtu.be/fis26HvvDII'],
                        ['Android App Development Specialization','https://www.coursera.org/specializations/android-app-development'],
                        ['Associate Android Developer Certification','https://grow.google/androiddev/#?modal_active=none'],
                        ['Become an Android Kotlin Developer by Udacity','https://www.udacity.com/course/android-kotlin-developer-nanodegree--nd940'],
                        ['Android Basics by Google','https://www.udacity.com/course/android-basics-nanodegree-by-google--nd803'],
                        ['The Complete Android Developer Course','https://www.udemy.com/course/complete-android-n-developer-course/'],
                        ['Building an Android App with Architecture Components','https://www.linkedin.com/learning/building-an-android-app-with-architecture-components'],
                        ['Android App Development Masterclass using Kotlin','https://www.udemy.com/course/android-oreo-kotlin-app-masterclass/'],
                        ['Flutter & Dart - The Complete Flutter App Development Course','https://www.udemy.com/course/flutter-dart-the-complete-flutter-app-development-course/'],
                        ['Flutter App Development Course [Free]','https://youtu.be/rZLR5olMR64']]

        ios_course = [['IOS App Development by LinkedIn','https://www.linkedin.com/learning/subscription/topics/ios'],
                    ['iOS & Swift - The Complete iOS App Development Bootcamp','https://www.udemy.com/course/ios-13-app-development-bootcamp/'],
                    ['Become an iOS Developer','https://www.udacity.com/course/ios-developer-nanodegree--nd003'],
                    ['iOS App Development with Swift Specialization','https://www.coursera.org/specializations/app-development'],
                    ['Mobile App Development with Swift','https://www.edx.org/professional-certificate/curtinx-mobile-app-development-with-swift'],
                    ['Swift Course by LinkedIn','https://www.linkedin.com/learning/subscription/topics/swift-2'],
                    ['Objective-C Crash Course for Swift Developers','https://www.udemy.com/course/objectivec/'],
                    ['Learn Swift by Codecademy','https://www.codecademy.com/learn/learn-swift'],
                    ['Swift Tutorial - Full Course for Beginners [Free]','https://youtu.be/comQ1-x2a1Q'],
                    ['Learn Swift Fast - [Free]','https://youtu.be/FcsY1YPBwzQ']]
        uiux_course = [['Google UX Design Professional Certificate','https://www.coursera.org/professional-certificates/google-ux-design'],
                    ['UI / UX Design Specialization','https://www.coursera.org/specializations/ui-ux-design'],
                    ['The Complete App Design Course - UX, UI and Design Thinking','https://www.udemy.com/course/the-complete-app-design-course-ux-and-ui-design/'],
                    ['UX & Web Design Master Course: Strategy, Design, Development','https://www.udemy.com/course/ux-web-design-master-course-strategy-design-development/'],
                    ['The Complete App Design Course - UX, UI and Design Thinking','https://www.udemy.com/course/the-complete-app-design-course-ux-and-ui-design/'],
                    ['DESIGN RULES: Principles + Practices for Great UI Design','https://www.udemy.com/course/design-rules/'],
                    ['Become a UX Designer by Udacity','https://www.udacity.com/course/ux-designer-nanodegree--nd578'],
                    ['Adobe XD Tutorial: User Experience Design Course [Free]','https://youtu.be/68w2VwalD5w'],
                    ['Adobe XD for Beginners [Free]','https://youtu.be/WEljsc2jorI'],
                    ['Adobe XD in Simple Way','https://learnux.io/course/adobe-xd']]

        resume_videos = ['https://youtu.be/y8YH0Qbu5h4','https://youtu.be/J-4Fv8nq1iA',
                        'https://youtu.be/yp693O87GmM','https://youtu.be/UeMmCex9uTU',
                        'https://youtu.be/dQ7Q8ZdnuN0','https://youtu.be/HQqqQx5BCFY',
                        'https://youtu.be/CLUsplI4xMU','https://youtu.be/pbczsLkv7Cc']

        interview_videos = ['https://youtu.be/Ji46s5BHdr0','https://youtu.be/seVxXHi2YMs',
                            'https://youtu.be/9FgfsLa_SmY','https://youtu.be/2HQmjLu-6RQ',
                            'https://youtu.be/DQd_AlIvHUw','https://youtu.be/oVVdezJ0e7w'
                            'https://youtu.be/JZK1MZwUyUU','https://youtu.be/CyXLhHQS3KY']
        # resume = cleanResume(resume)
except:
    st.write("")

def cleanResume(text):
    text = re.sub('http\S+\s*', ' ', text)  # remove URLs
    text = re.sub('RT|cc', ' ', text)  # remove RT and cc
    text = re.sub('#\S+', '', text)  # remove hashtags
    text = re.sub('@\S+', '  ', text)  # remove mentions
    text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', text)  # remove punctuations
    text = re.sub(r'[^\x00-\x7f]',r' ', text) 
    text = re.sub('\s+', ' ', text)  # remove extra whitespace
    return text
    
#logic
def getResult(JD_txt,resume_txt):
    content = [JD_txt,resume_txt]

    cv = CountVectorizer()

    matrix = cv.fit_transform(content)

    similarity_matrix =  cosine_similarity(matrix)

    match = similarity_matrix[0][1] * 100

    return match


#button 

if click:
    match = getResult(job_description_filtered_sentence1,resume_filtered_sentence1)
    match = round(match,2)
    st.write("Match Percentage: ",match,"%")
    st.write("Job description: \n", job_description_filtered_sentence1)
    st.write("Resume: \n ",resume_filtered_sentence1)
    # st.write(resume_filtered_sentence1list)
    if reco_field == 'Data Science':
        st.write('A Data Science Resume')
        st.write("** Our analysis says you are looking for Data Science Jobs.**")
        recommended_skills = ['Data Visualization','Predictive Analysis','Statistical Modeling','Data Mining','Clustering & Classification','Data Analytics','Quantitative Analysis','Web Scraping','ML Algorithms','Keras','Pytorch','Probability','Scikit-learn','Tensorflow',"Flask",'Streamlit']
        recommended_keywords = st.write('Recommended skills generated from System', recommended_skills)
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
        st.write("Recommended courses are: ", ds_course)
    elif reco_field == 'Web Development':
        st.write("** Our analysis says you are looking for Web Development Jobs **")
        recommended_skills = ['React','Django','Node JS','React JS','php','laravel','Magento','wordpress','Javascript','Angular JS','c#','Flask','SDK']
        recommended_keywords = st.write('Recommended skills generated from System',recommended_skills)
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
        st.write("Recommended courses are: ", web_course)
    elif reco_field == 'Android Development':
        st.write("** Our analysis says you are looking for Android App Development Jobs **")
        recommended_skills = ['Android','Android development','Flutter','Kotlin','XML','Java','Kivy','GIT','SDK','SQLite']
        recommended_keywords = st.write('Recommended skills generated from System',recommended_skills)
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)
        st.write("Recommended courses are: ", android_course)
    elif  reco_field == 'IOS Development':
        st.write("** Our analysis says you are looking for IOS App Development Jobs **")
        recommended_skills = ['IOS','IOS Development','Swift','Cocoa','Cocoa Touch','Xcode','Objective-C','SQLite','Plist','StoreKit',"UI-Kit",'AV Foundation','Auto-Layout']
        recommended_keywords = st.write('Recommended skills generated from System',recommended_skills)
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)        
        st.write("Recommended courses are: ", ios_course)
    elif reco_field == 'UI-UX Development':
        st.write("** Our analysis says you are looking for UI-UX Development Jobs **")
        recommended_skills = ['UI','User Experience','Adobe XD','Figma','Zeplin','Balsamiq','Prototyping','Wireframes','Storyframes','Adobe Photoshop','Editing','Illustrator','After Effects','Premier Pro','Indesign','Wireframe','Solid','Grasp','User Research']
        recommended_keywords = st.write('Recommended skills generated from System',recommended_skills)
        st.markdown('''<h4 style='text-align: left; color: #1ed760;'>Adding this skills to resume will boost🚀 the chances of getting a Job💼</h4>''',unsafe_allow_html=True)          
        st.write("Recommended courses are: ", uiux_course)
        
st.caption(" ~ made by JLA")
