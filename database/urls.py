"""database URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myuser.views import UserRegistrationView, MyLogin, MyProfile, UserRegisterViewByID
from lead.views import LeadAddView, LeadDetailView
from django.urls import path
from service.views import ServiceListView
from leadfollowup.views import LeadFollowupListCreateView, LeadFollowupDetailView
from payment.views import PaymentList, PaymentDetail,PaymentByLead
from paymentmode.views import MyPaymentMode
from paymenttype.views import MyPaymentType
from leadlastfollowup.views import LeadLastFollowupListCreateView,LeadLastFollowupDetailView
from customerstudent.views import CustomerList
from convertedstudent.views import ConvertedStudentList
from feetracer.views import FeeTrackerList,FeeTracerByPaymentID,FeeTrackekrkDetail
from leadlastfollowup.views import LeadLastFollowUpByLeadId
from navbar.views import MyNavbar
from django.conf.urls.static import static
from django.conf import settings
from refundfees.views import FeesRefundApiView
from paymentlink.views import PaymentLinkView, PaymentLinkViewGetUrl
from batch.views import BatchApiView, BatchApiViewById
from batchstudent.views import BatchStudentListView, BatchStudentByConvertedIdView
from brand.views import BrandApiViewById
# 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", UserRegistrationView.as_view(), name="register"),
    path("register/<int:id>/", UserRegisterViewByID.as_view(), name="register"),
    path("login/", MyLogin.as_view(), name="login"),
    path('profile/', MyProfile.as_view(), name='profile'),
    path('lead/', LeadAddView.as_view(), name='addlead'),
    path('brand/<int:id>/', BrandApiViewById.as_view(), name='brand'),
    path('lead/<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('services/<int:brand_id>/', ServiceListView.as_view(), name='service-list'),
    path('leadfollowup/', LeadFollowupListCreateView.as_view(), name='leadfollowup-list'),
    path('leadfollowup/<int:id>/', LeadFollowupListCreateView.as_view(), name='leadfollowup-detail'),
    path('leadlastfollowup/', LeadLastFollowupListCreateView.as_view(), name='leadlastfollowup-list'),
    path('leadlastfollowup/<int:pk>/', LeadLastFollowupListCreateView.as_view(), name='leadlastfollowup-detail'),
    path('leadlastfollowupbyid/<int:id>/',LeadLastFollowUpByLeadId.as_view(), name="LeadLastFollowUpById"),
    path('payments/', PaymentList.as_view(), name='payment-list'),
    path('payments/<int:id>/', PaymentList.as_view(), name='payment-detail'),
    path('paymentsbylead/<int:id>/', PaymentByLead.as_view(), name='payment-detail'),
    path('paymentmode/<int:brand_id>/',MyPaymentMode.as_view(), name="payment-mode"),
    path('paymenttype/<int:brand_id>/',MyPaymentType.as_view(), name="payment-type"),
    path('customer/', CustomerList.as_view(), name="Customer"),
    path('customer/<int:id>/', CustomerList.as_view(), name="CustomerList"),
    path('convertedlead/', ConvertedStudentList.as_view(), name="ConvertedStudentList"),
    path('convertedlead/<int:id>/', ConvertedStudentList.as_view(), name="ConvertedStudentList"),
    path('feetracer/', FeeTrackerList.as_view(), name="Feetracer"),
    path('feetracerpost/', FeeTrackekrkDetail.as_view(), name="FeePost"),
    path('feetracer/<int:id>/', FeeTrackerList.as_view(), name="Feetracer"),
    path('navbar/', MyNavbar.as_view(), name="navbar"),
    path('refundfees/',FeesRefundApiView.as_view(), name="refundfees"),
    path('refundfees/<int:id>/',FeesRefundApiView.as_view(), name="refundfees"),
    path('getfeesdetailspaymentid/<int:id>/',FeeTracerByPaymentID.as_view(), name="getfeesdetailbypaymentid"),
    path('paymentlink/',PaymentLinkView.as_view(), name="payment_link_view"),
    path('paymentlinkurl/',PaymentLinkViewGetUrl.as_view(), name="payment_link_view"),
    path('batch/', BatchApiView.as_view(), name="batch_link_view"),
    path('batch/<int:id>/', BatchApiViewById.as_view(), name="batch_api_view_by_id"),
    path('batchstudent/', BatchStudentListView.as_view(), name="batch_student"),
    path('batchstudent/<int:id>/',BatchStudentByConvertedIdView.as_view(),name="batchstudentbyconvertedid" )
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

