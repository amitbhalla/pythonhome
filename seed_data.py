import os
import django
import datetime

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amit_bhalla.settings')
django.setup()

from core.models import Service, Testimonial, CaseStudy, Resource, BlogPost, FAQ, ProcessStep
from django.utils import timezone

def create_seed_data():
    print("Creating seed data for the Amit Bhalla Marketing website...")
    
    # Clear existing data
    Service.objects.all().delete()
    Testimonial.objects.all().delete()
    CaseStudy.objects.all().delete()
    Resource.objects.all().delete()
    BlogPost.objects.all().delete()
    FAQ.objects.all().delete()
    ProcessStep.objects.all().delete()
    
    # Create Services
    services = [
        {
            'title': 'Marketing Strategy',
            'icon_class': 'fas fa-bullseye',
            'short_description': 'Comprehensive marketing plans customized to your business goals, industry, and target audience to drive sustainable growth.',
            'full_description': 'My marketing strategy service provides a comprehensive roadmap that aligns your marketing efforts with your business objectives. Through in-depth market research, competitor analysis, and customer insights, I develop a tailored strategy that positions your brand effectively, targets the right audience, and leverages the most appropriate channels for maximum impact. The result is a clear, actionable plan that drives sustainable growth and delivers measurable ROI.',
            'order': 1,
        },
        {
            'title': 'Growth Marketing',
            'icon_class': 'fas fa-chart-line',
            'short_description': 'Data-driven campaigns focused on rapid, sustainable growth, customer acquisition, and revenue optimization.',
            'full_description': 'Growth marketing combines creative marketing strategies with data-driven experimentation to accelerate your company\'s growth. Using a systematic approach, I identify the most effective acquisition channels, optimize conversion funnels, and implement retention strategies that maximize customer lifetime value. By continuously testing, measuring, and iterating, we create a scalable growth engine that delivers predictable results and a strong return on investment.',
            'order': 2,
        },
        {
            'title': 'Brand Development',
            'icon_class': 'fas fa-bullhorn',
            'short_description': 'Strategic brand development that differentiates your business, creates emotional connections, and builds customer loyalty.',
            'full_description': 'My brand development service helps you create a distinctive brand identity that resonates with your target audience and stands out in the marketplace. Through a strategic process that includes brand positioning, messaging framework, visual identity, and brand guidelines, I craft a cohesive brand that communicates your unique value proposition and builds lasting connections with customers. A strong brand doesn\'t just attract attention—it builds loyalty, commands premium pricing, and drives long-term business growth.',
            'order': 3,
        },
        {
            'title': 'Employer Branding',
            'icon_class': 'fas fa-users',
            'short_description': 'Attract top talent by building a compelling employer brand that showcases your culture and values to potential candidates.',
            'full_description': 'In today\'s competitive talent market, a strong employer brand is essential for attracting and retaining top talent. My employer branding service helps you develop a compelling employee value proposition, craft authentic storytelling that highlights your culture and values, and implement strategies to showcase your company as an employer of choice. By aligning your employer brand with your corporate brand, we create a cohesive identity that appeals to both customers and prospective employees.',
            'order': 4,
        },
    ]
    
    for service_data in services:
        Service.objects.create(**service_data)
    
    print(f"Created {len(services)} services")
    
    # Create Testimonials
    testimonials = [
        {
            'name': 'Sarah Johnson',
            'position': 'CMO',
            'company': 'TechFlow Solutions',
            'content': 'Amit completely transformed our marketing approach. He helped us implement a data-driven strategy that increased our conversion rates by 53% in just 3 months. His insights and expertise were invaluable, and our team learned so much from his guidance.',
            'order': 1,
        },
        {
            'name': 'Michael Chen',
            'position': 'Founder & CEO',
            'company': 'Horizon Ventures',
            'content': 'Working with Amit was a game-changer for our business. He helped us identify our unique market position and craft a marketing strategy that resonated with our ideal customers. Within 6 months, our lead generation increased by 215% and our sales pipeline grew significantly.',
            'order': 2,
        },
        {
            'name': 'Jessica Martinez',
            'position': 'VP Marketing',
            'company': 'Urban Lifestyle',
            'content': 'Amit\'s strategic approach to marketing helped us cut through the noise in a crowded market. His methodical process and deep understanding of consumer psychology led to messaging that truly resonated with our audience. Our brand awareness metrics improved by 78% and our customer acquisition cost dropped by 32%.',
            'order': 3,
        },
    ]
    
    for testimonial_data in testimonials:
        Testimonial.objects.create(**testimonial_data)
    
    print(f"Created {len(testimonials)} testimonials")
    
    # Create Case Studies
    case_studies = [
        {
            'title': 'SaaS Growth Acceleration',
            'client': 'TechFlow Solutions',
            'industry': 'B2B SaaS',
            'challenge': 'TechFlow Solutions, a B2B SaaS company, was struggling with high customer acquisition costs and low conversion rates despite having a superior product. Their marketing efforts were scattered across multiple channels without a cohesive strategy, resulting in inconsistent results and wasted resources.',
            'solution': 'I developed a comprehensive growth strategy focused on identifying the most efficient acquisition channels and optimizing the conversion funnel. This included repositioning their product messaging to emphasize key differentiators, implementing a content marketing strategy targeting specific pain points of their ideal customer profile, and creating a lead nurturing sequence that educated prospects about the value of their solution.',
            'results': 'Within 6 months, TechFlow Solutions achieved a 217% increase in monthly recurring revenue (MRR), reduced customer acquisition costs by 43%, and improved conversion rates from trial to paid by 37%. Their payback period decreased from 14 months to 5 months, significantly improving their unit economics and positioning them for sustainable growth.',
            'result_metrics': {
                'key_metric_1': {'value': '217%', 'label': 'MRR Growth'},
                'key_metric_2': {'value': '43%', 'label': 'CAC Reduction'}
            },
            'order': 1,
        },
        {
            'title': 'E-commerce Revenue Optimization',
            'client': 'Urban Lifestyle',
            'industry': 'E-commerce',
            'challenge': 'Urban Lifestyle, a direct-to-consumer apparel brand, was experiencing plateaued sales despite increasing their advertising spend. Their customer acquisition costs were rising, while conversion rates and average order values were declining. They needed a strategy to break through the growth ceiling and improve profitability.',
            'solution': 'I conducted a comprehensive audit of their marketing funnel and customer journey, identifying key drop-off points and opportunities for optimization. We implemented a multi-faceted approach including a refined targeting strategy, personalized email marketing campaigns, enhanced product bundling, and a customer loyalty program. We also revised their content strategy to build stronger emotional connections with their target audience.',
            'results': 'The results were transformative. Urban Lifestyle saw a 156% increase in revenue over 8 months, with a 3.2x return on ad spend (ROAS). Their average order value increased by 27%, and their customer retention rate improved by 34%. Most importantly, they established a predictable, scalable growth model that continued to deliver results beyond our engagement.',
            'result_metrics': {
                'key_metric_1': {'value': '156%', 'label': 'Revenue Increase'},
                'key_metric_2': {'value': '3.2x', 'label': 'ROAS'}
            },
            'order': 2,
        },
        {
            'title': 'B2B Lead Generation',
            'client': 'GlobalTech Solutions',
            'industry': 'Professional Services',
            'challenge': 'GlobalTech Solutions, a consulting firm specializing in digital transformation, was struggling to generate quality leads in a highly competitive market. Their previous marketing efforts resulted in high volumes of unqualified leads that rarely converted to sales, wasting valuable sales team resources and creating frustration.',
            'solution': 'I developed an integrated demand generation strategy focused on quality over quantity. This included creating targeted thought leadership content, implementing an account-based marketing approach for key industries, developing a lead scoring system to prioritize high-potential prospects, and designing nurture campaigns that educated prospects about their methodologies and results.',
            'results': 'Within 4 months, GlobalTech Solutions experienced a 189% increase in qualified leads, with a 37% improvement in lead-to-opportunity conversion rates. Their sales cycle shortened by 24%, and they secured three major enterprise clients that had previously been unresponsive to their outreach. The improved alignment between marketing and sales also resulted in more efficient resource allocation and higher team morale.',
            'result_metrics': {
                'key_metric_1': {'value': '189%', 'label': 'Lead Growth'},
                'key_metric_2': {'value': '37%', 'label': 'Conversion Lift'}
            },
            'order': 3,
        },
    ]
    
    for case_study_data in case_studies:
        CaseStudy.objects.create(**case_study_data)
    
    print(f"Created {len(case_studies)} case studies")
    
    # Create Resources
    resources = [
        {
            'title': 'Growth Marketing Framework',
            'resource_type': 'framework',
            'icon_class': 'fas fa-bullseye',
            'short_description': 'A comprehensive framework for planning, executing, and measuring marketing initiatives that drive sustainable business growth.',
            'order': 1,
        },
        {
            'title': 'Marketing ROI Calculator',
            'resource_type': 'template',
            'icon_class': 'fas fa-chart-line',
            'short_description': 'A detailed spreadsheet for tracking and calculating the return on investment for your marketing campaigns across multiple channels.',
            'order': 2,
        },
        {
            'title': 'Customer Persona Development Guide',
            'resource_type': 'guide',
            'icon_class': 'fas fa-users',
            'short_description': 'A step-by-step guide to creating detailed customer personas that drive effective targeting and messaging in your marketing campaigns.',
            'order': 3,
        },
        {
            'title': 'Marketing Campaign Launch Checklist',
            'resource_type': 'checklist',
            'icon_class': 'fas fa-tasks',
            'short_description': 'A comprehensive checklist to ensure you\'ve covered all aspects of planning and executing a successful marketing campaign.',
            'order': 4,
        },
        {
            'title': 'Content Strategy Blueprint',
            'resource_type': 'ebook',
            'icon_class': 'fas fa-book',
            'short_description': 'A detailed guide to developing a content strategy that attracts, engages, and converts your target audience through valuable content.',
            'order': 5,
        },
        {
            'title': 'Email Marketing Sequence Templates',
            'resource_type': 'template',
            'icon_class': 'fas fa-envelope',
            'short_description': 'Ready-to-use email sequence templates for customer onboarding, lead nurturing, and re-engagement campaigns.',
            'order': 6,
        },
    ]
    
    for resource_data in resources:
        Resource.objects.create(**resource_data)
    
    print(f"Created {len(resources)} resources")
    
    # Create Blog Posts
    blog_posts = [
        {
            'title': '5 Data-Driven Marketing Strategies That Actually Work',
            'slug': '5-data-driven-marketing-strategies-that-actually-work',
            'excerpt': 'Discover five proven marketing strategies backed by data that can significantly improve your conversion rates and ROI.',
            'category': 'Marketing Strategy',
            'tags': 'data-driven, marketing strategy, ROI, analytics, conversion optimization',
            'author': 'Amit Bhalla',
            'read_time': 8,
            'content': """
# 5 Data-Driven Marketing Strategies That Actually Work

In today's competitive business landscape, intuition alone isn't enough to guide your marketing efforts. Successful marketing campaigns are increasingly reliant on data-driven strategies that provide measurable results and clear ROI.

## 1. Customer Segmentation and Personalization

One of the most effective data-driven strategies is customer segmentation. By dividing your audience into distinct groups based on behaviors, demographics, or purchase history, you can create highly targeted campaigns that resonate with each segment.

**Implementation tip:** Start with 3-5 core segments and create personalized messaging for each. Even simple personalization can increase conversion rates by 10-15%.

## 2. Conversion Rate Optimization (CRO)

CRO is the systematic process of increasing the percentage of website visitors who take desired actions. This data-driven approach uses A/B testing, user behavior analysis, and optimization techniques to improve performance.

**Implementation tip:** Focus on one page or funnel step at a time, starting with high-traffic areas. Small improvements in conversion rates can lead to significant revenue increases.

## 3. Content Marketing with Performance Tracking

Content marketing becomes truly powerful when paired with robust analytics. By tracking which content pieces drive engagement, leads, and conversions, you can refine your strategy for maximum impact.

**Implementation tip:** Implement UTM parameters and conversion tracking to measure each content piece's performance, then double down on formats and topics that deliver results.

## 4. Remarketing and Behavioral Targeting

Remarketing targets users who have previously interacted with your brand but haven't converted. This strategy leverages behavioral data to deliver relevant messages to prospects at the right time.

**Implementation tip:** Create specialized remarketing campaigns for different user behaviors (product views, cart abandonment, etc.) with messaging that addresses potential objections.

## 5. Predictive Analytics for Customer Lifetime Value

Predictive analytics helps identify which customers are likely to be most valuable in the long term, allowing you to allocate resources more efficiently.

**Implementation tip:** Develop a simple CLV model based on purchase frequency, average order value, and customer lifespan to prioritize acquisition and retention efforts.

## Conclusion

Data-driven marketing isn't just about collecting information—it's about turning that information into actionable insights that drive growth. By implementing these five strategies, you'll be able to make more informed decisions, optimize your marketing spend, and deliver measurable results for your business.

Remember that becoming data-driven is a journey, not a destination. Start with one strategy, measure your results, learn from the data, and continuously optimize for improvement.
            """,
            'date': timezone.now().date() - datetime.timedelta(days=7),
            'is_published': True,
        },
        {
            'title': 'How to Build a Marketing Strategy That Actually Drives Growth',
            'slug': 'how-to-build-a-marketing-strategy-that-actually-drives-growth',
            'excerpt': 'Learn the key components of an effective marketing strategy that aligns with your business goals and delivers sustainable growth.',
            'category': 'Marketing Strategy',
            'tags': 'strategy, marketing plan, growth, business objectives, competitive advantage',
            'author': 'Amit Bhalla',
            'read_time': 10,
            'content': """
# How to Build a Marketing Strategy That Actually Drives Growth

Many businesses approach marketing as a series of disconnected tactics rather than a cohesive strategy. This leads to wasted resources, inconsistent messaging, and disappointing results. In this post, I'll outline how to build a marketing strategy that creates real business impact.

## Start with Clear Business Objectives

Your marketing strategy must be directly tied to your business goals. Are you looking to:

- Increase market share in a specific segment?
- Enter a new market?
- Launch a new product or service?
- Improve customer retention and lifetime value?

Defining clear objectives provides direction for your entire marketing strategy and establishes metrics for measuring success.

## Deeply Understand Your Audience

Successful marketing strategies are built on customer insights. Develop detailed buyer personas that go beyond basic demographics to understand:

- Pain points and challenges
- Goals and aspirations
- Decision-making processes
- Content preferences and consumption habits
- Objections and concerns

These insights will inform everything from messaging to channel selection.

## Conduct a Thorough Competitive Analysis

Understanding your competitive landscape helps you identify opportunities to differentiate your brand and offering. Analyze:

- Direct and indirect competitors
- Their positioning and messaging
- Pricing strategies
- Marketing channels and tactics
- Strengths and weaknesses

This analysis will help you find gaps in the market that your brand can fill.

## Develop a Distinctive Value Proposition

Your value proposition should clearly communicate why customers should choose you over alternatives. It should be:

- Relevant to your target audience's needs
- Specific about the benefits you provide
- Different from your competitors' offerings
- Simple and easy to understand

This becomes the foundation of all your marketing messages.

## Create a Multi-Channel Marketing Plan

Based on your audience research, identify the most effective channels to reach your target customers. Your plan should include:

- Content strategy aligned with the buyer's journey
- Digital marketing tactics (SEO, PPC, social media, email)
- Traditional marketing when appropriate
- Channel-specific goals and KPIs

Ensure your messaging is consistent across all channels while being optimized for each platform.

## Implement Measurement and Optimization Processes

A truly effective marketing strategy includes systems for ongoing measurement and improvement:

- Define key performance indicators (KPIs) for each tactic
- Establish regular reporting schedules
- Create a process for analyzing results
- Build feedback loops for continuous optimization

## Conclusion

Building a marketing strategy that drives growth isn't about following the latest trends or copying competitors. It's about making informed, strategic decisions based on your business objectives, audience needs, and competitive landscape.

Remember that strategy development isn't a one-time event. The most successful businesses regularly review and refine their marketing strategies as market conditions change and new data becomes available.

By following this framework, you'll develop a marketing strategy that not only guides your tactical execution but genuinely contributes to business growth.
            """,
            'date': timezone.now().date() - datetime.timedelta(days=14),
            'is_published': True,
        },
        {
            'title': 'The ROI of Brand Building: Why Long-Term Thinking Pays Off',
            'slug': 'the-roi-of-brand-building-why-long-term-thinking-pays-off',
            'excerpt': 'Explore how investing in brand building delivers significant returns over time and why businesses should balance short-term tactics with long-term brand strategies.',
            'category': 'Brand Development',
            'tags': 'branding, ROI, marketing strategy, long-term growth, brand equity',
            'author': 'Amit Bhalla',
            'read_time': 12,
            'content': """
# The ROI of Brand Building: Why Long-Term Thinking Pays Off

In an era of quarterly targets and immediate results, brand building often takes a backseat to short-term performance marketing. However, the most successful businesses understand that sustainable growth requires balancing short-term activation with long-term brand building.

## The Short-Term Bias in Marketing

Many businesses prioritize marketing activities that deliver immediate, measurable results:

- Conversion-focused digital ads
- Sales promotions and discounts
- Direct response campaigns
- Bottom-of-funnel content

While these tactics are important, they become less effective and more expensive over time without the foundation of a strong brand.

## The Evidence for Long-Term Brand Building

Research by Les Binet and Peter Field analyzed thousands of marketing campaigns and found that:

- Brand-building campaigns deliver larger business effects that increase over time
- Short-term activation campaigns show immediate results that decay quickly
- The optimal balance is roughly 60% brand building and 40% activation
- Brand-building amplifies the effectiveness of activation campaigns

## How Brand Building Creates Financial Value

Strong brands create significant business value through multiple mechanisms:

### 1. Price Premium

Customers are willing to pay more for brands they trust and value. According to research, strong brands can command price premiums of 13-18% compared to weaker competitors.

### 2. Customer Acquisition Efficiency

Strong brands enjoy lower customer acquisition costs because:

- Prospects are already familiar with and predisposed toward the brand
- Word-of-mouth recommendations reduce paid media requirements
- Higher conversion rates improve marketing efficiency

### 3. Customer Retention and Loyalty

Customers are less likely to switch from brands they feel emotionally connected to, leading to:

- Higher customer lifetime value
- Reduced churn rates
- More stable revenue streams

### 4. Resilience During Challenges

Strong brands recover faster from crises and market disruptions. During economic downturns, strong brands typically lose less market share and recover more quickly.

## Measuring Brand Building ROI

While brand building effects are longer-term, they can and should be measured:

- Brand awareness tracking
- Brand perception studies
- Share of voice monitoring
- Customer acquisition cost trends
- Price sensitivity analysis
- Customer lifetime value changes

## Finding the Right Balance

The optimal approach is not choosing between brand building and performance marketing but finding the right balance:

1. Establish clear brand positioning and messaging
2. Invest consistently in building brand awareness and associations
3. Use performance marketing to convert the interest generated by brand activities
4. Measure both short-term activation metrics and long-term brand metrics
5. Adjust the balance based on your market position and business objectives

## Conclusion

While short-term marketing tactics provide the gratification of immediate results, sustainable business growth requires investment in long-term brand building. The most successful businesses recognize that these approaches are complementary, not competitive.

By taking a balanced approach that nurtures your brand while driving conversions, you'll create a marketing engine that delivers both immediate results and enduring competitive advantage.
            """,
            'date': timezone.now().date() - datetime.timedelta(days=21),
            'is_published': True,
        },
    ]
    
    for blog_post_data in blog_posts:
        BlogPost.objects.create(**blog_post_data)
    
    print(f"Created {len(blog_posts)} blog posts")
    
    # Create FAQs
    faqs = [
        {
            'question': 'How do your marketing services differ from traditional agencies?',
            'answer': 'Unlike traditional agencies that focus primarily on execution, I take a holistic approach to marketing strategy. I work directly with leadership teams to align marketing initiatives with business goals, develop comprehensive frameworks for sustainable growth, and ensure all tactics are data-driven and measurable. My approach is more strategic and consultative, focusing on long-term success rather than just short-term campaigns.',
            'order': 1,
        },
        {
            'question': 'What types of businesses do you typically work with?',
            'answer': 'I work with growth-oriented businesses across various industries, including SaaS, e-commerce, professional services, and B2B companies. My clients typically range from funded startups looking to scale rapidly to established mid-market companies seeking to optimize their marketing ROI and build sustainable growth engines. The common thread is a commitment to data-driven marketing and a desire for strategic guidance beyond tactical execution.',
            'order': 2,
        },
        {
            'question': 'How do you measure marketing success?',
            'answer': 'I believe in establishing clear KPIs and metrics that align with your specific business goals. Depending on your objectives, these might include customer acquisition cost (CAC), customer lifetime value (LTV), conversion rates, lead quality, revenue growth, or ROI. We\'ll determine the most relevant metrics for your business at the outset and establish a measurement framework to track progress over time. Regular reporting and analysis ensure we can optimize strategies based on real performance data.',
            'order': 3,
        },
        {
            'question': 'What is your typical engagement process?',
            'answer': 'My engagement process typically follows these steps:\n\n1. **Discovery and Analysis**: I\'ll conduct a thorough assessment of your current marketing efforts, business goals, target audience, and competitive landscape.\n\n2. **Strategy Development**: Based on the analysis, I\'ll create a customized marketing strategy aligned with your business objectives.\n\n3. **Implementation Planning**: We\'ll develop a detailed roadmap for executing the strategy, including timelines, resources, and key milestones.\n\n4. **Execution Support**: I can either work with your internal team or help you manage external resources to implement the strategy.\n\n5. **Measurement and Optimization**: We\'ll continuously monitor performance, make data-driven adjustments, and optimize for better results.',
            'order': 4,
        },
        {
            'question': 'How long does it typically take to see results?',
            'answer': 'The timeline for results varies depending on your current marketing maturity, industry, and specific goals. Some tactical improvements may show results within weeks, while strategic initiatives typically begin showing meaningful results within 3-6 months. What\'s important is that we\'ll establish clear expectations upfront and track leading indicators that signal progress before the final results manifest. Marketing is both an art and a science—we\'ll focus on building sustainable growth rather than quick fixes that don\'t last.',
            'order': 5,
        },
    ]
    
    for faq_data in faqs:
        FAQ.objects.create(**faq_data)
    
    print(f"Created {len(faqs)} FAQs")
    
    # Create Process Steps
    process_steps = [
        {
            'title': 'Discovery & Analysis',
            'description': 'Comprehensive audit of your current marketing efforts, business goals, target audience, and competitive landscape to identify opportunities.',
            'icon_class': 'fas fa-search',
            'order': 1,
        },
        {
            'title': 'Strategy Development',
            'description': 'Creating a customized marketing strategy that addresses your specific challenges and leverages your unique advantages in the market.',
            'icon_class': 'fas fa-pencil-ruler',
            'order': 2,
        },
        {
            'title': 'Implementation',
            'description': 'Execution of the marketing plan with precision, ensuring all elements work together cohesively to achieve your business objectives.',
            'icon_class': 'fas fa-rocket',
            'order': 3,
        },
        {
            'title': 'Measurement & Optimization',
            'description': 'Continuous monitoring of performance metrics to measure results against KPIs and refine strategies for maximum effectiveness.',
            'icon_class': 'fas fa-chart-line',
            'order': 4,
        },
    ]
    
    for process_step_data in process_steps:
        ProcessStep.objects.create(**process_step_data)
    
    print(f"Created {len(process_steps)} process steps")
    
    print("Seed data creation complete!")

if __name__ == '__main__':
    create_seed_data()
