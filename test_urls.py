#!/usr/bin/env python
"""
URL Testing Script for Yellow Key AMRC
Tests all URLs for 404, 500, and other errors
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yk.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

# Add testserver to ALLOWED_HOSTS
from django.conf import settings
if 'testserver' not in settings.ALLOWED_HOSTS:
    settings.ALLOWED_HOSTS.append('testserver')

from django.test import Client
from django.contrib.auth import get_user_model
from accounts.models import Profile, Roles
from property.models import Property_data, Zone_names, Portions, Portions_status
from django.urls import reverse

User = get_user_model()

class URLTester:
    def __init__(self):
        self.client = Client()
        self.results = {
            'success': [],
            'redirect': [],
            'client_error': [],
            'server_error': [],
            'not_found': []
        }
        self.setup_test_data()

    def setup_test_data(self):
        """Create test user and data"""
        print("Setting up test data...")

        # Create test user
        self.user = User.objects.filter(username='testuser').first()
        if not self.user:
            self.user = User.objects.create_user(
                username='testuser',
                email='test@yellowkey.qa',
                password='testpass123'
            )

        # Create profile
        if not hasattr(self.user, 'profile'):
            Profile.objects.create(
                user=self.user,
                username='testuser',
                email='test@yellowkey.qa'
            )

        # Create test property data
        self.property = Property_data.objects.filter(user=self.user).first()
        if not self.property:
            self.property = Property_data.objects.create(
                user=self.user,
                title='Test Property',
                client_code='TEST001',
                property_code='PROP001',
                landmark='Test Landmark',
                zone_no=67,
                street_no=45,
                property_no=123
            )

        # Create test portion
        self.portion = Portions.objects.filter(property_data=self.property).first()
        if not self.portion:
            self.portion = Portions.objects.create(
                property_data=self.property,
                user=self.user,
                unit_no=101,
                floor_no=1,
                description='Test portion',
                price=5000,
                bedrooms=2,
                bathrooms=1,
                portion_type='2BHK',
                furnished_type='Furnished',
                sqft=1000
            )

        print(f"[OK] Test user created: {self.user.username}")
        print(f"[OK] Test property created: {self.property.title}")
        print(f"[OK] Test portion created: Unit {self.portion.unit_no}")

    def test_url(self, url, name, requires_auth=False, method='GET', expected_status=None):
        """Test a single URL"""
        try:
            if requires_auth:
                self.client.force_login(self.user)

            if method == 'GET':
                response = self.client.get(url, follow=False)
            elif method == 'POST':
                response = self.client.post(url, follow=False)

            status = response.status_code

            # Categorize result
            if expected_status and status == expected_status:
                category = 'success'
            elif status == 200:
                category = 'success'
            elif status in [301, 302, 303, 307, 308]:
                category = 'redirect'
            elif status == 404:
                category = 'not_found'
            elif 400 <= status < 500:
                category = 'client_error'
            elif status >= 500:
                category = 'server_error'
            else:
                category = 'success'

            self.results[category].append({
                'url': url,
                'name': name,
                'status': status,
                'method': method
            })

            return status

        except Exception as e:
            self.results['server_error'].append({
                'url': url,
                'name': name,
                'status': 'ERROR',
                'error': str(e),
                'method': method
            })
            return 'ERROR'

    def test_all_urls(self):
        """Test all URLs from all apps"""

        print("\n" + "="*80)
        print("TESTING ALL URLS")
        print("="*80 + "\n")

        # PUBLIC URLS (No authentication required)
        print("Testing PUBLIC URLs...")
        public_urls = [
            ('/', 'home'),
            ('/about/', 'about'),
            ('/contact/', 'contact'),
            ('/services/', 'services'),
            ('/property_services/', 'property_services'),
            ('/workman_services/', 'workman_services'),
            ('/realtor_services/', 'realtor_services'),
            ('/careers/', 'careers_list'),
            ('/accounts/login/', 'account_login'),
            ('/accounts/signup/', 'account_signup'),
            ('/robots.txt', 'robots'),
            ('/sitemap.xml', 'sitemap'),
            ('/api/health/', 'api_health'),
        ]

        for url, name in public_urls:
            status = self.test_url(url, name, requires_auth=False)
            print(f"  {status} - {url} ({name})")

        # AUTHENTICATED URLS
        print("\nTesting AUTHENTICATED URLs...")
        auth_urls = [
            # Accounts (mounted at root, not /accounts/)
            ('/profile/', 'profile'),
            ('/profile/update/', 'profile_update'),

            # Property
            ('/property/', 'property_all'),
            (f'/property/{self.user.id}/', 'property_own'),
            ('/property/inquire/lists/', 'inquire_lists'),

            # Clients
            ('/clients/dashboard/', 'clients_dashboard'),
            ('/clients/dashboard/property/all/', 'property_all_list'),
            ('/clients/dashboard/property/own/', 'property_own_list'),
            ('/clients/dashboard/property/add/', 'property_create'),
            ('/clients/dashboard/portions/', 'portions_all_list'),
            (f'/clients/dashboard/{self.property.id}/portions/', 'portions_a_building'),

            # Realtor
            ('/realtor/', 'realtor_dashboard'),
            ('/realtor/vacant-portions/', 'realtor_vacant_portions'),
            ('/realtor/vacants/', 'realtor_vacants'),
            ('/realtor/inquiries/', 'realtor_inquiries'),
            ('/realtor/contacts/', 'realtor_contacts'),

            # Workman
            ('/workman/', 'workman_dashboard'),

            # Help
            ('/help/', 'help'),
            ('/help/client/', 'client_help'),
            ('/help/realtor/', 'realtor_help'),
            ('/help/workman/', 'workman_help'),

            # Webpages
            ('/dashboard/', 'choose_dashboard'),
        ]

        for url, name in auth_urls:
            status = self.test_url(url, name, requires_auth=True)
            print(f"  {status} - {url} ({name})")

        # PARAMETRIC URLS (URLs with dynamic parameters)
        print("\nTesting PARAMETRIC URLs...")
        parametric_urls = [
            # Property with IDs
            (f'/property/{self.user.id}/{self.property.id}/all/', 'portions_of_property'),
            (f'/property/{self.user.id}/{self.property.id}/{self.portion.id}/details/', 'portion_single_details'),

            # Clients with IDs
            (f'/clients/dashboard/property/update/{self.property.id}/', 'property_update'),
            (f'/clients/dashboard/{self.property.id}/portions/add/', 'portions_add'),
            (f'/clients/dashboard/portions/{self.portion.id}/update/', 'portions_update'),
        ]

        for url, name in parametric_urls:
            status = self.test_url(url, name, requires_auth=True)
            print(f"  {status} - {url} ({name})")

    def print_summary(self):
        """Print test results summary"""
        print("\n" + "="*80)
        print("TEST RESULTS SUMMARY")
        print("="*80 + "\n")

        total = sum(len(v) for v in self.results.values())

        print(f"Total URLs tested: {total}\n")

        # Success
        if self.results['success']:
            print(f"[OK] SUCCESS (200 OK): {len(self.results['success'])}")
            for item in self.results['success'][:5]:  # Show first 5
                print(f"  - {item['url']} ({item['status']})")
            if len(self.results['success']) > 5:
                print(f"  ... and {len(self.results['success']) - 5} more")

        # Redirects
        if self.results['redirect']:
            print(f"\n[->] REDIRECTS (3xx): {len(self.results['redirect'])}")
            for item in self.results['redirect']:
                print(f"  - {item['url']} ({item['status']}) - {item['name']}")

        # Not Found
        if self.results['not_found']:
            print(f"\n[X] NOT FOUND (404): {len(self.results['not_found'])}")
            for item in self.results['not_found']:
                print(f"  - {item['url']} - {item['name']}")

        # Client Errors
        if self.results['client_error']:
            print(f"\n[X] CLIENT ERRORS (4xx): {len(self.results['client_error'])}")
            for item in self.results['client_error']:
                print(f"  - {item['url']} ({item['status']}) - {item['name']}")

        # Server Errors
        if self.results['server_error']:
            print(f"\n[XX] SERVER ERRORS (5xx): {len(self.results['server_error'])}")
            for item in self.results['server_error']:
                error_msg = item.get('error', 'Unknown error')
                print(f"  - {item['url']} ({item['status']}) - {item['name']}")
                print(f"    Error: {error_msg}")

        # Summary
        print("\n" + "="*80)
        success_rate = (len(self.results['success']) / total * 100) if total > 0 else 0
        print(f"Success Rate: {success_rate:.1f}%")

        issues = len(self.results['not_found']) + len(self.results['client_error']) + len(self.results['server_error'])
        if issues == 0:
            print("[OK] No errors found! All URLs are working correctly.")
        else:
            print(f"[!] Found {issues} issues that need attention.")

        print("="*80)

    def generate_report(self):
        """Generate detailed report file"""
        report_path = 'url_test_report.txt'

        with open(report_path, 'w') as f:
            f.write("="*80 + "\n")
            f.write("YELLOW KEY AMRC - URL TEST REPORT\n")
            f.write("="*80 + "\n\n")

            for category, items in self.results.items():
                if items:
                    f.write(f"\n{category.upper().replace('_', ' ')} ({len(items)}):\n")
                    f.write("-" * 80 + "\n")
                    for item in items:
                        f.write(f"URL: {item['url']}\n")
                        f.write(f"Name: {item['name']}\n")
                        f.write(f"Status: {item['status']}\n")
                        if 'error' in item:
                            f.write(f"Error: {item['error']}\n")
                        f.write("\n")

        print(f"\n[OK] Detailed report saved to: {report_path}")

def main():
    print("="*80)
    print("YELLOW KEY AMRC - URL TESTING TOOL")
    print("="*80)

    tester = URLTester()
    tester.test_all_urls()
    tester.print_summary()
    tester.generate_report()

    print("\nURL testing complete!")

if __name__ == '__main__':
    main()
