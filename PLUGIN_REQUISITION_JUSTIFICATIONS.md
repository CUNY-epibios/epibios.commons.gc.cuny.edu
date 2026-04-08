# Plugin Requisition Justifications
## CUNY Academic Commons - Department of Epidemiology & Biostatistics

**Date**: February 28, 2026
**Department**: Epidemiology and Biostatistics, CUNY School of Public Health
**Site**: https://epibios.commons.gc.cuny.edu/
**Requested By**: [Your Name]

---

## Executive Summary

As part of implementing our department website redesign, we have identified **3 critical plugins** that are not currently available in the CUNY Academic Commons plugin library. All three have **free versions** available and would significantly enhance the site's functionality, security, and usability.

**Requested Plugins**:
1. **User Role Editor** (Free) - For faculty page editing permissions
2. **Wordfence Security** (Free) - For site security and FERPA compliance
3. **UpdraftPlus** (Free) - For backup/disaster recovery

**Total Cost**: $0 (using free versions)

---

## Requisition #1: User Role Editor

### Plugin Information
- **Name**: User Role Editor
- **Version**: 4.64+ (latest)
- **Developer**: Vladimir Garagulya
- **WordPress.org URL**: https://wordpress.org/plugins/user-role-editor/
- **License**: GPL v2+ (Free)
- **Active Installations**: 900,000+
- **Rating**: 4.8/5 stars (1,700+ reviews)
- **Last Updated**: Actively maintained

### Why This Plugin Is Critical

#### Use Case
Our site requires **14 faculty members** to edit their own profile pages without accessing admin functions or editing other faculty pages. WordPress's built-in "Author" role is insufficient because:

1. **Authors can edit ALL their own posts**: If a faculty member authors multiple pages, they can edit any of them. We need each faculty member to edit ONLY one specific page.

2. **No admin menu customization**: Authors see unnecessary menu items (Posts, Comments, Tools) that confuse non-technical users and increase support burden.

3. **No capability granularity**: Can't grant permissions like "edit only this specific page" or "upload images but not edit theme."

#### Specific Functionality Needed
- Create custom "Faculty Member" role with exact capabilities needed
- Restrict faculty to editing ONLY their assigned page
- Hide unnecessary admin menu items per role
- Provide clean, simplified admin interface for non-technical users

#### Alternative Solutions Considered
| Alternative | Why Not Suitable | Cost |
|------------|------------------|------|
| WordPress Built-in Roles | Too coarse, no page-specific control | Free |
| Custom Code Development | $2,000-5,000 upfront + maintenance | $2,000+ |
| PublishPress Capabilities | More features but costs money | $79/year |
| WordPress Multisite | Over-engineered for our needs | Free but complex |

#### Risk if Not Approved
- Faculty may accidentally edit wrong pages
- Increased support tickets from confused faculty
- Potential for faculty to access inappropriate admin functions
- Need to invest $2,000+ in custom development
- Poor user experience discourages faculty participation

#### Security Considerations
- **Actively maintained**: Last updated within past month
- **Large user base**: 900,000+ active installations
- **Well-reviewed**: 4.8/5 stars, vetted by community
- **Open source**: GPL license, code auditable
- **Compatible**: Works with WordPress 6.0+

#### Benefits to CUNY Commons
- Could benefit other departments with similar needs
- Free plugin with wide adoption
- Reduces custom code requirements across network
- Improves user experience for faculty contributors

### Recommended Action
**Approve installation of User Role Editor (Free version)** to plugin library

---

## Requisition #2: Wordfence Security

### Plugin Information
- **Name**: Wordfence Security – Firewall, Malware Scan, and Login Security
- **Version**: 7.11+ (latest)
- **Developer**: Wordfence (Defiant Inc.)
- **WordPress.org URL**: https://wordpress.org/plugins/wordfence/
- **License**: GPL v3 (Free core version)
- **Active Installations**: 4,000,000+
- **Rating**: 4.7/5 stars (3,600+ reviews)
- **Last Updated**: Actively maintained

### Why This Plugin Is Critical

#### Use Case
Our site will host **sensitive course evaluation data** subject to FERPA regulations. Current security gaps:

1. **No brute force protection**: WordPress login is vulnerable to automated attacks
2. **No firewall**: No protection against malicious requests
3. **No malware scanning**: Can't detect if site is compromised
4. **No security monitoring**: No visibility into attack attempts
5. **No 2FA enforcement**: Can't require two-factor authentication

**NOTE**: We understand **Jetpack** is available in CUNY Commons. However:
- Unclear if CUNY subscription includes Jetpack Security features
- Wordfence provides more comprehensive security specifically
- Request clarification on Jetpack capabilities before proceeding

#### Specific Functionality Needed (Free Version)
- **Firewall**: Blocks malicious traffic before reaching WordPress
- **Malware scanner**: Daily scans for compromised files
- **Login security**: Rate limiting, 2FA support, CAPTCHA
- **Live traffic monitoring**: See attack attempts in real-time
- **Security event logging**: Audit trail for compliance

#### FERPA Compliance Considerations
- Course evaluations contain student information
- Must protect against unauthorized access
- Need audit trail of login attempts
- Required for IRB data protection policies

#### Risk if Not Approved
- **High risk of data breach**: Course evaluations exposed
- **FERPA compliance issues**: May violate federal regulations
- **Reputational damage**: Breach could harm department and CUNY
- **Lost faculty trust**: Faculty won't submit evaluations to insecure site
- **Legal liability**: Potential lawsuits if student data exposed

#### Security Considerations
- **Industry leader**: Most popular WordPress security plugin
- **4 million+ installations**: Widely trusted
- **Free version sufficient**: Premium ($119/year) not needed for our use case
- **Actively maintained**: Updates within days of security issues
- **Vetted by community**: Recommended by WordPress.org

#### Questions for CUNY IT
Before approving Wordfence, please clarify:
1. Does CUNY provide network-level security that covers our needs?
2. Is Jetpack Security included in CUNY's subscription?
3. Are there existing CUNY policies that address WordPress security?

### Recommended Action
**Option 1**: Confirm Jetpack Security features are adequate
**Option 2**: Approve Wordfence Security (Free version) if Jetpack insufficient

---

## Requisition #3: UpdraftPlus

### Plugin Information
- **Name**: UpdraftPlus: WP Backup & Migration Plugin
- **Version**: 1.24+ (latest)
- **Developer**: UpdraftPlus.Com, DavidAnderson
- **WordPress.org URL**: https://wordpress.org/plugins/updraftplus/
- **License**: GPL v3 (Free)
- **Active Installations**: 3,000,000+
- **Rating**: 4.8/5 stars (5,800+ reviews)
- **Last Updated**: Actively maintained

### Why This Plugin Is Critical

#### Use Case
Our site will contain **unique, irreplaceable content**:
- 14 faculty research profiles
- Custom course evaluation forms and data
- Student research publications database
- Internal department documents

**Current backup status**: UNKNOWN
- Need clarification: Does CUNY Commons provide automated backups?
- If yes: What is restore procedure? How far back?
- If no: Site has NO backup/disaster recovery capability

#### Specific Functionality Needed (Free Version)
- **Automated backups**: Schedule daily/weekly
- **Offsite storage**: Backup to Google Drive, Dropbox, or email
- **One-click restore**: Recover from disaster quickly
- **Database + files**: Complete site backup
- **Manual backup**: Before major changes

#### Disaster Scenarios Without Backups
| Scenario | Impact Without Backup | Recovery |
|----------|---------------------|----------|
| Hacked site | Complete data loss | Rebuild from scratch (weeks) |
| Bad plugin update | Site breaks, data corrupted | Restore from backup (minutes) |
| Accidental deletion | Faculty profile lost | Restore individual page |
| Server failure | All course evaluations lost | NO RECOVERY POSSIBLE |
| Bad code edit | Site crashes | Restore to pre-edit state |

#### Risk if Not Approved
- **Catastrophic data loss**: Years of course evaluations irretrievable
- **Weeks of downtime**: Rebuilding site from scratch
- **Lost research content**: Faculty publications and profiles gone
- **Reputation damage**: Faculty won't trust the platform
- **Wasted development time**: All work can be lost in seconds

#### Questions for CUNY IT
**CRITICAL - MUST ANSWER BEFORE IMPLEMENTATION**:
1. Does CUNY Commons provide automated backups of individual sites?
2. If yes:
   - What is the backup schedule? (daily/weekly?)
   - How many backup versions retained?
   - What is the restore procedure?
   - Can we restore a single page or must restore entire site?
   - Can we trigger manual backups before major changes?
3. If no:
   - How are we expected to handle disaster recovery?
   - Is UpdraftPlus or similar available?

#### Alternative Solutions
If CUNY provides adequate backups:
- Document restore procedure thoroughly
- Test restore process quarterly
- No plugin needed

If CUNY does NOT provide backups:
- **UpdraftPlus (Free)**: Best option, easiest to use
- **BackWPup (Free)**: Alternative, more complex
- **Manual backups**: Extremely error-prone, not recommended
- **No backups**: UNACCEPTABLE RISK

#### Security Considerations
- **3 million+ installations**: Industry standard
- **Highly rated**: 4.8/5 stars
- **Actively maintained**: Frequent updates
- **Free version sufficient**: Premium ($70/year) not needed
- **Data ownership**: Backups stored in OUR cloud accounts

### Recommended Action
**Priority 1**: Contact CUNY IT to clarify backup capabilities
**Priority 2**: If CUNY backups inadequate, approve **UpdraftPlus (Free version)**

---

## Summary Table

| Plugin | Purpose | Cost | Risk if Missing | Priority |
|--------|---------|------|----------------|----------|
| **User Role Editor** | Faculty page editing | FREE | Medium - Poor UX, increased support | HIGH |
| **Wordfence Security** | Site security, FERPA | FREE | HIGH - Data breach, compliance | CRITICAL |
| **UpdraftPlus** | Backup/recovery | FREE | CATASTROPHIC - Permanent data loss | CRITICAL |

---

## Recommended Approval Process

### Immediate (Week 1)
1. **Clarify with CUNY IT**:
   - Jetpack Security features available
   - Backup capabilities and restore procedure
   - Network-level security protections

### Short-term (Week 2-3)
2. **Based on CUNY IT responses**:
   - If Jetpack Security adequate: Proceed without Wordfence
   - If backups provided: Document procedure, no plugin needed
   - If gaps exist: Request plugin approvals

### Plugin Approval Priority
If plugins are needed:
1. **UpdraftPlus** (if no backups) - CRITICAL
2. **Wordfence** (if no security) - CRITICAL
3. **User Role Editor** - HIGH

---

## Technical Specifications

All requested plugins meet CUNY standards:

| Requirement | User Role Editor | Wordfence | UpdraftPlus |
|-------------|-----------------|-----------|-------------|
| **License** | GPL v2+ ✓ | GPL v3 ✓ | GPL v3 ✓ |
| **Free Version** | Yes ✓ | Yes ✓ | Yes ✓ |
| **WordPress.org** | Yes ✓ | Yes ✓ | Yes ✓ |
| **Active Development** | Yes ✓ | Yes ✓ | Yes ✓ |
| **PHP 7.4+ Compatible** | Yes ✓ | Yes ✓ | Yes ✓ |
| **WordPress 6.0+** | Yes ✓ | Yes ✓ | Yes ✓ |
| **Multisite Compatible** | Yes ✓ | Yes ✓ | Yes ✓ |
| **Security Audited** | Community ✓ | Professional ✓ | Community ✓ |
| **Privacy Compliant** | Yes ✓ | Yes ✓ | Yes ✓ |

---

## Expected Outcomes

### With Approved Plugins
- ✅ Faculty can safely edit their own pages
- ✅ Site protected against attacks and breaches
- ✅ Course evaluations secured (FERPA compliant)
- ✅ Disaster recovery capability
- ✅ Professional user experience
- ✅ Reduced IT support burden

### Without Approved Plugins
- ❌ Risk of faculty editing wrong content
- ❌ Vulnerable to security breaches
- ❌ FERPA compliance concerns
- ❌ No disaster recovery (permanent data loss risk)
- ❌ Poor user experience, high support needs
- ❌ Need for expensive custom development ($2,000+)

---

## Additional Notes

### Open Source Commitment
All requested plugins are:
- Free and open source (GPL licensed)
- Available on WordPress.org official repository
- No vendor lock-in
- Code can be audited by CUNY IT

### Multisite Compatibility
All plugins are tested and compatible with WordPress Multisite, which CUNY Commons uses.

### No Premium Features Needed
We've carefully evaluated that the **FREE versions** of all three plugins meet our needs. Premium versions offer features we don't require.

### Benefit to Other CUNY Sites
These plugins could benefit other department sites on CUNY Commons:
- Many sites need role management for multiple contributors
- All sites benefit from security and backups
- One approval benefits entire network

---

## Conclusion

We respectfully request approval for installation of these three free, open-source plugins to the CUNY Academic Commons plugin library. All three address critical needs:

1. **User Role Editor**: Improves UX and reduces support burden
2. **Wordfence Security**: Protects sensitive data and ensures FERPA compliance
3. **UpdraftPlus**: Provides disaster recovery capability

Alternatively, we request clarification on:
- CUNY Commons backup capabilities and procedures
- Jetpack Security features included in CUNY subscription
- Network-level security protections already in place

**Total additional cost**: $0
**Risk reduction**: HIGH
**Time to implement**: 1 week after approval

Thank you for considering this request. Please contact us with any questions or to discuss alternatives.

---

## Contact Information

**Department**: Epidemiology and Biostatistics
**School**: CUNY School of Public Health
**Site URL**: https://epibios.commons.gc.cuny.edu/
**Technical Contact**: [Your Name]
**Email**: [Your Email]
**Phone**: [Your Phone]

---

## Appendix: Alternative Plugins Considered

If the requested plugins cannot be approved, these alternatives could be considered:

### For User Management
- **Members** (already available in CUNY Commons) - Limited but may work
- **Restricted Site Access** - Different approach
- Custom development - $2,000-5,000

### For Security
- **Jetpack Security** - If included in CUNY subscription
- **Sucuri Security** - Alternative security plugin (also free)
- **iThemes Security** - Another option (free version)

### For Backups
- **BackWPup** - More complex but free
- **Manual backups** - Very error-prone
- CUNY Commons network backups - If available

We selected our requested plugins based on:
- Largest user base (most trusted)
- Best ratings and reviews
- Easiest to use and maintain
- Most complete free versions
- Best documentation and support
